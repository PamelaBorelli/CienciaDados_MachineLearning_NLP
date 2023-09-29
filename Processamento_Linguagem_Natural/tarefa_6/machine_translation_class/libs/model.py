import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
import numpy as np

class NMTModel(nn.Module):
	# neural machine translation model
	def __init__(self, source_vocab_size, source_embedding_size,
		target_vocab_size, target_embedding_size, encoding_size,
		target_bos_index):
		super(NMTModel, self).__init__()
		# source_vocab_size: number of unique words in source language
		# source_embedding_size: embedding dimension for source lang
		# target_vocab_sizenumber of unique words in target language
		# target_embedding_size: embedding dimension for target lang
		# encoding_size: dim of the hidden state of the encoder rnn
		# target_bos_index: index for begin-of-sequence token

		self.encoder = NMTEncoder(num_embeddings = source_vocab_size,
								embedding_size = source_embedding_size,
								rnn_hidden_size = encoding_size)

		# encoder is a bidirectional rnn
		decoding_size = encoding_size * 2

		self.decoder = NMTDecoder(num_embeddings = target_vocab_size,
								embedding_size = target_embedding_size,
								rnn_hidden_size = decoding_size,
								bos_index = target_bos_index)

	def forward(self, x_source, x_source_lenghts, target_sequence, sample_probability=0.0, max_sequence_size=None):
		# forward pass

		encoder_state, final_hidden_states = self.encoder(x_source,
														x_source_lenghts)

		decoded_states = self.decoder(encoder_state = encoder_state,
									initial_hidden_state = final_hidden_states,
									target_sequence = target_sequence,
									sample_probability=sample_probability,
									max_sequence_size=max_sequence_size)

		return decoded_states


class NMTEncoder(nn.Module):
	def __init__(self, num_embeddings, embedding_size, rnn_hidden_size):
		super(NMTEncoder, self).__init__()
		# num_embeddings is the size of the vocabulary
		# embedding_size is the dimension of embedding vectors
		# rnn_hidden_size is the size of the RNN hidden states

		self.source_embedding = nn.Embedding(num_embeddings, embedding_size, padding_idx=0)

		self.birnn = nn.GRU(embedding_size, rnn_hidden_size, bidirectional=True, batch_first=True)

	def forward(self, x_source, x_lengths):
		# x_source.shape: # (batch, max_len)

		x_embedded = self.source_embedding(x_source) # (batch, max_len, embed_size)

		x_lengths = x_lengths.detach().cpu().numpy()

		# https://pytorch.org/docs/stable/generated/torch.nn.utils.rnn.pad_packed_sequence.html
		x_packed = pack_padded_sequence(x_embedded, x_lengths, batch_first=True)

		# x_birnn_out.shape (if it was unpacked): (batch_size, L, 2*hidden_size)
		x_birnn_out, x_birnn_h = self.birnn(x_packed)
		
		# first dimension is 2 because it is bidirectional - 2 hidden states
		# x_birnn_h.shape: (2, batch_size, hidden_size)
		# permute to (batch_size, 2, hidden_size)
		x_birnn_h = x_birnn_h.permute(1,0,2)

		# flatten to x_birnn_h.shape: (batch_size, 2*hidden_size)
		x_birnn_h = x_birnn_h.contiguous().view(x_birnn_h.size(0), -1)

		# to the reverse operation to pack_padded_sequence
		# sequence_unpacked, lengths_unpacked
		x_unpacked, _ = pad_packed_sequence(x_birnn_out, batch_first=True)
		# x_unpacked.shape: (batch_size, L_batch, 2*hidden_size)
		# L here is reduced to the largest sequence length without padding for the batch

		return x_unpacked, x_birnn_h

class NMTDecoder(nn.Module):
	def __init__(self, num_embeddings, embedding_size, 
		rnn_hidden_size, bos_index):
		super(NMTDecoder, self).__init__()
		# num_embeddings is the size of the target vocabulary
		# embedding_size is the dimension of embedding vectors
		# rnn_hidden_size is the size of the decoder RNN hidden states
		# bos_index: begin-of-sequence index

		self._rnn_hidden_size = rnn_hidden_size
		self.target_embedding = nn.Embedding(num_embeddings = num_embeddings,
										embedding_dim = embedding_size,
										padding_idx = 0)

		# the input to the GRU will be the embedding vector concatenated with the previous
		# context vector
		self.gru_cell = nn.GRUCell(embedding_size + rnn_hidden_size, rnn_hidden_size)

		self.hidden_map = nn.Linear(rnn_hidden_size, rnn_hidden_size)
		self.classifier = nn.Linear(rnn_hidden_size * 2, num_embeddings)

		self.bos_index = bos_index

		# any small constant will be fine
		# self._sampling_temperature = 3

	def _init_indices(self, batch_size):
		# return the BEGIN-OF-SEQUENCE index vector
		return torch.ones(batch_size, dtype=torch.int64) * self.bos_index

	def _init_context_vectors(self, batch_size):
		# return a zero vector for initializing the context
		# this vector is attention weighted sum calculated in later time-steps
		return torch.zeros(batch_size, self._rnn_hidden_size)

	def forward(self, encoder_state, initial_hidden_state, target_sequence, sample_probability=0.0, max_sequence_size=None):

		if target_sequence is None:
			sample_probability = 1.0
			# use its own prediction to feed back at the rnn
			output_sequence_size = max_sequence_size
		else:

			# the target sequence shape is before permuting (batch, seq)
			# we want to iterate over the sequence, so we permute it to (seq, batch)
			target_sequence = target_sequence.permute(1,0)

			output_sequence_size = target_sequence.size(0)

		# use the provided encoder hidden state as the initial
		# hidden state
		h_t = self.hidden_map(initial_hidden_state)

		batch_size = encoder_state.size(0)
		# initialize context vectors to zero
		context_vectors = self._init_context_vectors(batch_size)
		# initialize first y_t word as BOS - for use in case of sampling
		candidate_input = self._init_indices(batch_size)

		h_t = h_t.to(encoder_state.device)
		context_vectors = context_vectors.to(encoder_state.device)
		candidate_input = candidate_input.to(encoder_state.device)

		output_vectors = []

		for i in range(output_sequence_size):

			use_sample = np.random.random() < sample_probability
			if not use_sample:
				y_t_index = target_sequence[i]
			else:
				y_t_index = candidate_input

			# step 1: Embed word and concat with previous context
			# y_input_vector.shape: (batch_size, embed_size)
			y_input_vector = self.target_embedding(y_t_index)

			# rnn_input.shape: (batch_size, embed_size+decoder_hidden_size)
			rnn_input = torch.cat([y_input_vector, context_vectors], dim=1)

			# step 2: make GRU step, getting a new hidden vector
			# h_t.shape: (batch_size, decoder_hidden_size)
			h_t = self.gru_cell(rnn_input, h_t)

			# step 3: use current hidden vector to attend to encoder state
			# context_vectors.shape: (8, 200)
			# probability_attention.shape: (8, 14)
			context_vectors = explicit_attention(encoder_state, query_vector=h_t) # context_vectors, p_attn

			# step 4: use current hidden and context vectors to
			# make prediction of next word
			prediction_vector = torch.cat((context_vectors, h_t), dim=1)

			# score_for_y_t_index.shape: (batch_size, target_vocab_size)
			score_for_y_t_index = self.classifier(prediction_vector)

			# I think this conditional is wrong, and should be removed -
			# if it should not use the sampled word, the conditional in the beginning of the loop
			# will take care of it
			# if use_sample:

			# sampling temperature forces a peakier distribution
			# p_y_t_index = F.softmax(score_for_y_t_index * self._sampling_temperature, dim=1)
			p_y_t_index = F.softmax(score_for_y_t_index, dim=1)

			# method 1: choose most likely word
			_, candidate_input = torch.max(p_y_t_index, 1)

			# method 2: sample from distribution
			# candidate_input = torch.multinomial(p_y_t_index, 1).squeeze()

			# collect the prediction scores
			output_vectors.append(score_for_y_t_index)

		# shape before permuting: (L, batch_size, target_vocab_size)
		# shape after permuting: (batch_size, L, target_vocab_size)
		output_vectors = torch.stack(output_vectors).permute(1, 0, 2)

		return output_vectors

def explicit_attention(encoder_state_vectors, query_vector):
	# query_vector.shape: (batch_size, 2*encoder_hidden_size)
	# encoder_state_vectors.shape: (batch_size, L, 2*encoder_hidden_size)

	batch_size, num_vectors, vector_size = encoder_state_vectors.size()

	# make the dot product of the query vector with the encoder state vectors
	# vector_scores.shape: (batch_size, L)
	vector_scores = torch.sum(encoder_state_vectors * query_vector.view(batch_size, 1, vector_size), dim=2)

	# vector_probabilities.shape: (batch_size, L)
	vector_probabilities = F.softmax(vector_scores, dim=1)

	# weighted_vectors: (batch_size, L, 2*encoder_hidden_size)
	weighted_vectors = encoder_state_vectors * vector_probabilities.view(batch_size, num_vectors, 1)

	# context_vectors: (batch_size, 2*encoder_hidden_size)
	context_vectors = torch.sum(weighted_vectors, dim=1)

	return context_vectors

def attention(encoder_state_vectors, query_vector):
	# query_vector.shape: (batch_size, 2*hidden_size
	# encoder_state_vectors: (batch_size, L, 2*hidden_size)

	# vector_scores (batch_size, L, 1) = 
	# encoder_state_vectors (batch_size, L, 2*hidden_size) x query_vector (batch_size, 2*hidden_size, 1)
	vector_scores = torch.matmul(encoder_state_vectors,
		query_vector.unsqueeze(dim=2)).squeeze()

	vector_probabilities = F.softmax(vector_scores, dim=-1)

	# context_vectors (batch_size, 2*hidden_size, 1) = 
	# encoder_state_vectors.T (batch_size, 2*hidden_size, L) x vector_probabilities (batch_size, L, 1)
	context_vectors = torch.matmul(encoder_state_vectors.transpose(-2,-1),
		vector_probabilities.unsqueeze(dim=2)).squeeze()

	return context_vectors



