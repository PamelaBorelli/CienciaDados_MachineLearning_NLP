from libs.nlpclasses import NMTDataset
from libs.utils import generate_nmt_batches
from libs.utils import monitor_training
# from libs.utils import make_train_state
from libs.utils import NMTSampler
from libs.model import NMTModel

import torch
import numpy as np

import argparse

# caminho para o modelo que se quer avaliar
model_path = None

# atualizar hiperparâmetros
dataset_csv = "machine_translation_class\data\simplest_eng_fra.csv"
source_embedding_size= None
target_embedding_size= None
encoding_size= None
batch_size= None 
learning_rate= None
num_epochs= None


# source_embedding_size=24
# target_embedding_size=24
# encoding_size=32
# batch_size=32
# learning_rate=0.0005
# l2_regularization = 0.001
# num_epochs=40


if not torch.cuda.is_available():
	device = torch.device("cpu")
else:
	device = torch.device("cuda")
print("[INFO] using device: {}".format(device))

# dataset and vectorizer
dataset = NMTDataset.load_dataset_and_make_vectorizer(dataset_csv)
vectorizer = dataset.get_vectorizer()

# model
model = NMTModel(source_vocab_size=len(vectorizer.source_vocab), 
	source_embedding_size=source_embedding_size,
	target_vocab_size=len(vectorizer.target_vocab), 
	target_embedding_size=target_embedding_size, 
	encoding_size=encoding_size,
	target_bos_index=vectorizer.target_vocab.begin_seq_index)

model = model.to(device)

# get the mask index to pass to the funtion that calculates the loss
mask_index = vectorizer.target_vocab.mask_index

print("[INFO] loading model...")
state = torch.load("checkpoints/{}".format(model_path))
model.load_state_dict(state["model_state"])

model = model.eval().to(device)

sampler = NMTSampler(vectorizer, model)

dataset.set_split('test')
batch_generator = generate_nmt_batches(dataset, 
	batch_size=batch_size,
	device=device)

# change to false if you don't want to see samples of the translation
print_samples = True

test_results = []
for batch_dict in batch_generator:
	sampler.apply_to_batch(batch_dict, sample_probability=1.0)
	for i in range(batch_size):
		test_results.append(sampler.get_ith_item(i, False))
		if print_samples:
		# if you want to print some of the translations
			if i % 1000 == 0:
				source = test_results[-1]['source']
				reference = test_results[-1]['reference']
				sampled = test_results[-1]['sampled']

				source = " ".join(source)
				reference = " ".join(reference)
				sampled = " ".join(sampled)

				print("---- source / reference / sampled")
				print(source)
				print(reference)
				print(sampled)

bleu_list = [r['bleu-4'] for r in test_results]

mean_bleu = np.mean(bleu_list)
median_bleu = np.median(bleu_list)

print("[INFO] mean result: {}, median result: {}".format(mean_bleu, median_bleu))






