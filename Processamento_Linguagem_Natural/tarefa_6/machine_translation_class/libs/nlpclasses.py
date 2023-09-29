from torch.utils.data import Dataset
import pandas as pd
import numpy as np

class Vocabulary(object):
	# class to process text and extract vocabulary for mapping
	def __init__(self):

		self._token_to_idx = {}
		self._idx_to_token = {}

	def add_token(self, token):
		# updates mapping based on token
		if token in self._token_to_idx:
			index = self._token_to_idx[token]
		else:
			index = len(self._token_to_idx)
			self._token_to_idx[token] = index
			self._idx_to_token[index] = token
		return index

	def add_many(self, tokens):
		# add a list of tokens to the vocabulary
		return [self.add_token(token) for token in tokens]

	def lookup_token(self, token):
		# retrieve the index associated with the token
		# or the UNK index if token isn't present
		return self._token_to_idx[token]

	def lookup_index(self, index):
		# return the token associated with the index
		if index not in self._idx_to_token:
			raise KeyError("the index {} is not in the Vocabulary".format(index))
		return self._idx_to_token[index]

	def __len__(self):
		return len(self._token_to_idx)

class SequenceVocabulary(Vocabulary):
	def __init__(self, unk_token="<UNK>",
		mask_token="<MASK>", begin_seq_token="<BEGIN>",
		end_seq_token="<END>"):
		super(SequenceVocabulary, self).__init__()

		self._mask_token = mask_token
		self._unk_token = unk_token
		self._begin_seq_token = begin_seq_token
		self._end_seq_token = end_seq_token

		self.mask_index = self.add_token(self._mask_token)
		self.unk_index = self.add_token(self._unk_token)
		self.begin_seq_index = self.add_token(self._begin_seq_token)
		self.end_seq_index = self.add_token(self._end_seq_token)

	def lookup_token(self, token):
		return self._token_to_idx.get(token, self.unk_index)

class NMTVectorizer(object):
	def __init__(self, source_vocab, target_vocab, max_source_length,
		max_target_length):
		# source_vocab: SequenceVocabulary
		# target_vocab: SequenceVocabulary
		# max_source_length: longest sequence size
		# max_target_length: longest sequence size

		self.source_vocab = source_vocab
		self.target_vocab = target_vocab

		self.max_source_length = max_source_length
		self.max_target_length = max_target_length

	@classmethod
	def from_dataframe(cls, bitext_df):
		# bitext_df: parallel text dataset

		source_vocab = SequenceVocabulary()
		target_vocab = SequenceVocabulary()

		max_source_length = 0
		max_target_length = 0

		for _, row in bitext_df.iterrows():

			source_tokens = row["source_language"].split(" ")
			if len(source_tokens) > max_source_length:
				max_source_length = len(source_tokens)
			for token in source_tokens:
				source_vocab.add_token(token)

			target_tokens = row["target_language"].split(" ")
			if len(target_tokens) > max_target_length:
				max_target_length = len(target_tokens)
			for token in target_tokens:
				target_vocab.add_token(token)

		return cls(source_vocab, target_vocab, 
			max_source_length, max_target_length)

	# vectorize method agnostic to target or source sequence
	def _vectorize(self, indices, vector_length=-1, mask_index=0):
		# indices (list) : list of integers that represent a sequence
		# vector_length (int): forces the length of the index vector
		# mask_index (int): mask index to use

		if vector_length < 0:
			vector_length = len(indices)

		vector = np.zeros(vector_length, dtype=np.int64)
		vector[:len(indices)] = indices
		vector[len(indices):] = mask_index

		return vector

	def _get_source_indices(self, text):
		# return vectorized source text

		indices = [self.source_vocab.begin_seq_index]
		indices.extend(self.source_vocab.lookup_token(token)
			for token in text.split(" "))
		indices.append(self.source_vocab.end_seq_index)
		return indices

	def _get_target_indices(self, text):
		# return vectorized target text

		indices = [self.target_vocab.lookup_token(token)
			for token in text.split(" ")]
		x_indices = [self.target_vocab.begin_seq_index] + indices
		y_indices = indices + [self.target_vocab.end_seq_index]
		return x_indices, y_indices

	def vectorize(self, source_text, target_text, use_dataset_max_lenghts=True):

		source_vector_lenght = -1
		target_vector_lenght = -1

		if use_dataset_max_lenghts:
			source_vector_lenght = self.max_source_length + 2
			target_vector_lenght = self.max_target_length + 1

		source_indices = self._get_source_indices(source_text)
		source_vector = self._vectorize(source_indices,
			vector_length = source_vector_lenght,
			mask_index = self.source_vocab.mask_index)

		target_x_indices, target_y_indices = self._get_target_indices(target_text)

		target_x_vector = self._vectorize(target_x_indices,
			vector_length = target_vector_lenght,
			mask_index = self.target_vocab.mask_index)

		target_y_vector = self._vectorize(target_y_indices,
			vector_length = target_vector_lenght,
			mask_index = self.target_vocab.mask_index)

		return {"source_vector": source_vector,
				"target_x_vector": target_x_vector,
				"target_y_vector": target_y_vector,
				"source_length": len(source_indices)}


class NMTDataset(Dataset):

	def __init__(self, text_df, vectorizer):
		# review_df: pandas dataframe
		# vectorizer: ReviewVectorizer object

		self.text_df = text_df
		self._vectorizer = vectorizer

		self.train_df = self.text_df[self.text_df.split=='train']
		self.train_size = len(self.train_df)

		self.val_df = self.text_df[self.text_df.split=='val']
		self.validation_size = len(self.val_df)

		self.test_df = self.text_df[self.text_df.split=='test']
		self.test_size = len(self.test_df)

		self._lookup_dict = {
			'train': (self.train_df, self.train_size),
			'val': (self.val_df, self.validation_size),
			'test': (self.test_df, self.test_size)
		}

		self.set_split('train')

	@classmethod
	def load_dataset_and_make_vectorizer(cls, dataset_csv):
		# args: dataset_csv: location of the dataset
		# returns: an instance of the Dataset

		text_df = pd.read_csv(dataset_csv)
		train_subset = text_df[text_df.split=='train']
		return cls(text_df, NMTVectorizer.from_dataframe(train_subset))

	def get_vectorizer(self):
		# returns the vectorizer
		return self._vectorizer

	def set_split(self, split="train"):
		# select the splits in the dataset
		self._target_split = split
		self._target_df, self._target_size = self._lookup_dict[split]

	def __len__(self):
		return self._target_size

	def __getitem__(self, index):
		# args: index (int): index to the data point
		# returns a dict holding the datapoint features (x_data)
		# and label (y_target)

		row = self._target_df.iloc[index]

		vector_dict = self._vectorizer.vectorize(row.source_language, 
			row.target_language)

		return {'x_source': vector_dict["source_vector"],
				'x_target': vector_dict["target_x_vector"],
				'y_target': vector_dict["target_y_vector"],
				'x_source_length': vector_dict["source_length"]}

	def get_num_batches(self, batch_size):
		# return number of batches in the dataset
		return len(self) // batch_size
