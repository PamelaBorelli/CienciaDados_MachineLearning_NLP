import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import torch
from torch.utils.data import DataLoader
import numpy as np

from nltk.translate import bleu_score

def sentence_from_indices(indices, vocab, strict=True, return_string=True):
	ignore_indices = set([vocab.mask_index, vocab.begin_seq_index, vocab.end_seq_index])
	out = []

	for index in indices:
		if index == vocab.begin_seq_index and strict:
			continue
		elif index == vocab.end_seq_index and strict:
			break
		else:
			out.append(vocab.lookup_index(index))
	if return_string:
		return " ".join(out)
	else:
		return out

# avoid harsh behaviour when no ngram overlaps are found using smoothing function
chencherry = bleu_score.SmoothingFunction()

class NMTSampler:
	def __init__(self, vectorizer, model):
		self.vectorizer = vectorizer
		self.model = model

	def apply_to_batch(self, batch_dict, sample_probability=0.0):
		self._last_batch = batch_dict

		y_pred = self.model(batch_dict["x_source"], 
			batch_dict["x_source_length"],
			batch_dict["x_target"],
			sample_probability=sample_probability)

		self._last_batch['y_pred'] = y_pred

	def _get_source_sentence(self, index, return_string=True):
		indices = self._last_batch['x_source'][index].cpu().detach().numpy()

		vocab = self.vectorizer.source_vocab
		return sentence_from_indices(indices, vocab, return_string=return_string)

	def _get_reference_sentence(self, index, return_string=True):
		indices = self._last_batch['y_target'][index].cpu().detach().numpy()

		vocab = self.vectorizer.target_vocab
		return sentence_from_indices(indices, vocab, return_string=return_string)

	def _get_sampled_sentence(self, index, return_string=True):
		_, all_indices = torch.max(self._last_batch['y_pred'], dim=2)
		sentence_indices = all_indices[index].cpu().detach().numpy()
		vocab = self.vectorizer.target_vocab
		return sentence_from_indices(sentence_indices, vocab, return_string=return_string)

	def get_ith_item(self, index, return_string=True):
		output = {"source": self._get_source_sentence(index, return_string=return_string),
				"reference": self._get_reference_sentence(index, return_string=return_string),
				"sampled": self._get_sampled_sentence(index, return_string=return_string)}

		reference = output['reference']
		hypothesis = output['sampled']

		if not return_string:
			reference = " ".join(reference)
			hypothesis = " ".join(hypothesis)

		output['bleu-4'] = bleu_score.sentence_bleu(
			references=[reference],
			hypothesis=hypothesis,
			smoothing_function=chencherry.method1)

		return output

def generate_nmt_batches(dataset, batch_size, shuffle=True, drop_last=True, device='cpu'):

	dataloader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=shuffle, drop_last=drop_last)

	# cada exemplo é um dicionário como esse:
	# {
	# 		'x_source': vector_dict["source_vector"],
	# 		'x_target': vector_dict["target_x_vector"],
	# 		'y_target': vector_dict["target_y_vector"],
	# 		'x_source_length': vector_dict["source_length"]
	# }
	for data_dict in dataloader:

		lengths = data_dict['x_source_length'].numpy()

		sorted_length_indices = lengths.argsort()[::-1].tolist()

		out_data_dict = {}

		for name, tensor in data_dict.items():

			out_data_dict[name] = data_dict[name][sorted_length_indices].to(device)

		yield out_data_dict

def monitor_training(H, path_loss, path_acc):
	plt.style.use("ggplot")
	plt.figure()
	plt.plot(np.arange(0, len(H["train_loss"])), H["train_loss"], label="train_loss")
	plt.plot(np.arange(0, len(H["val_loss"])), H["val_loss"], label="val_loss")	
	plt.title("Training Loss and Accuracy")
	plt.xlabel("Epoch #")
	plt.ylabel("Loss/Accuracy")
	plt.legend()
	plt.savefig(path_loss)
	plt.close()

	plt.style.use("ggplot")
	plt.figure()
	plt.plot(np.arange(0, len(H["train_acc"])), H["train_acc"], label="train_acc")
	plt.plot(np.arange(0, len(H["val_acc"])), H["val_acc"], label="val_acc")	
	plt.title("Training Loss and Accuracy")
	plt.xlabel("Epoch #")
	plt.ylabel("Loss/Accuracy")
	plt.legend()
	plt.savefig(path_acc)
	plt.close()		

# def make_train_state(model, optimizer, learning_rate):
#     # Initialize a dictionary to store the state
#     train_state = {}
#     # Store the model parameters
#     train_state["model"] = model.state_dict()
#     # Store the optimizer state
#     train_state["optimizer"] = optimizer.state_dict()
#     # Store the learning rate
#     train_state["learning_rate"] = learning_rate
#     # Store the loss values
#     train_state["loss"] = []
#     # Store the accuracy values
#     train_state["accuracy"] = []
#     # Return the train state
#     return train_state



