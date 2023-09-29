from libs.utils import *
from libs.nlpclasses import *
from libs.model import *

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch

import numpy as np

def normalize_size(y_pred, y_true):

	# y_pred: [batch_size * seq_len, vocab_index]
	y_pred = y_pred.contiguous().view(-1, y_pred.size(2))

	# y_true: [batch_size * seq_len]
	y_true = y_true.contiguous().view(-1)

	return y_pred, y_true

def sequence_loss(y_pred, y_true, mask_index):
	# y_pred: [batch_size, seq_len, vocab_index]
	# y_true: [batch_size, seq_len]

	y_pred, y_true = normalize_size(y_pred, y_true)

	return F.cross_entropy(y_pred, y_true, ignore_index=mask_index)

def compute_accuracy(y_pred, y_true, mask_index):

	y_pred, y_true = normalize_size(y_pred, y_true)

	# y_pred: [batch_size * seq_len, vocab_index]
	_, y_pred_indices = y_pred.max(dim=1)

	correct_indices = torch.eq(y_pred_indices, y_true).float()

	valid_indices = torch.ne(y_true, mask_index).float()

	n_correct = (correct_indices * valid_indices).sum().item()
	n_valid = valid_indices.sum().item()

	return n_correct/n_valid * 100

dataset_csv = "data\simplest_eng_fra.csv"
save_dir = "checkpoints\model.tar"
path_loss = "checkpoints/try1_loss.png"
path_acc = "checkpoints/try1_acc.png"


source_embedding_size=24
target_embedding_size=24
encoding_size=32
batch_size=32
num_epochs=40
learning_rate=0.00005
l2_regularization = 0.00001

train_state = {
	'epoch_index': 0,
	'train_loss': [],
	'train_acc': [],
	'val_loss': [],
	'val_acc': [],
}

if not torch.cuda.is_available():
	device = torch.device("cpu")
else:
	device = torch.device("cuda")
print("[INFO] using device {}".format(device))

# dataset e vetorizador
dataset = NMTDataset.load_dataset_and_make_vectorizer(dataset_csv)
vectorizer = dataset.get_vectorizer()
model = NMTModel(source_vocab_size=len(vectorizer.source_vocab),
                 source_embedding_size=source_embedding_size,
                 target_vocab_size=len(vectorizer.target_vocab),
                 target_embedding_size=target_embedding_size,
                 encoding_size=encoding_size,
                 target_bos_index=vectorizer.target_vocab.begin_seq_index)
model = model.to(device)
print(model)
# loss and optimizer (Adam, SGD, etc)
loss_func = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(),
                       lr=learning_rate,
                       weight_decay=l2_regularization)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer=optimizer,
                                           mode='min', factor=0.5,
                                           patience=1)
mask_index = vectorizer.target_vocab.mask_index
dataset.set_split('train')
dataset.set_split('val')

best_val_loss = 99999.9
for epoch_index in range(num_epochs):
  train_state['epoch_index'] = epoch_index

  # Iterate over training dataset

  # setup: batch generator, set loss and acc to 0, set train mode on
  dataset.set_split('train')
  batch_generator = generate_nmt_batches(dataset,batch_size=batch_size,
                                         device=device)
  running_loss = 0.0
  running_acc = 0.0
  model.train()

  for batch_index, batch_dict in enumerate(batch_generator):
    # the training routine is these 5 steps:

    # --------------------------------------
    # step 1. zero the gradients
    optimizer.zero_grad()
    # step 2. compute the output
    y_pred = model(batch_dict['x_source'],batch_dict['x_source_length'],
                   batch_dict['x_target'])

    # step 3. compute the loss
    loss = sequence_loss(y_pred, batch_dict['y_target'], mask_index)
    # Regularização L2
    loss += l2_regularization * sum(p.pow(2.0).sum() for p in model.parameters())

    # step 4. use loss to produce gradients
    loss.backward()

    # step 5. use optimizer to take gradient step
    optimizer.step()
    # -----------------------------------------
    # compute the running loss and running accuracy
    running_loss += (loss.item() - running_loss) / (batch_index + 1)

    acc_t = compute_accuracy(y_pred, batch_dict['y_target'], mask_index)
    running_acc += (acc_t - running_acc) / (batch_index + 1)

  train_state['train_loss'].append(running_loss)
  train_state['train_acc'].append(running_acc)

  # Iterate over val dataset

  # setup: batch generator, set loss and acc to 0; set eval mode on
  dataset.set_split('val')
  batch_generator = generate_nmt_batches(dataset,batch_size=batch_size,
                                           device=device)
  running_loss = 0.
  running_acc = 0.
  model.eval()

  for batch_index, batch_dict in enumerate(batch_generator):
    # compute the output
    y_pred = model(batch_dict['x_source'],batch_dict['x_source_length'],
                     batch_dict['x_target'])

    # step 3. compute the loss
    loss = sequence_loss(y_pred, batch_dict['y_target'], mask_index)

    # compute the running loss and accuracy
    running_loss += (loss.item() - running_loss) / (batch_index + 1)

    acc_t = compute_accuracy(y_pred, batch_dict['y_target'], mask_index)
    running_acc += (acc_t - running_acc) / (batch_index + 1)

  train_state['val_loss'].append(running_loss)
  train_state['val_acc'].append(running_acc)

  scheduler.step(train_state['val_loss'][-1])
  print("[INFO] epoch {}, train loss {}, val loss {}".format(epoch_index,
                                                               train_state['train_loss'][-1],
                                                               train_state['val_loss'][-1]))
  print("[INFO] train_acc {}, val acc {}".format(train_state['train_acc'][-1],
                                                   train_state['val_acc'][-1]))

  monitor_training(train_state, path_loss, path_acc)

  if best_val_loss > train_state['val_loss'][-1]:
    best_val_loss = train_state['val_loss'][-1]
    state = {'epoch': epoch_index,'model_state': model.state_dict(),
             'optimizer_state': optimizer.state_dict(),'metrics': train_state
		}
    torch.save(state, save_dir)
    print("[INFO] best validation loss updated and checkpoint saved")

# Evaluate NMT

# caminho para o modelo que se quer avaliar
model_path = save_dir

# atualizar hiperparâmetros
dataset_csv = dataset_csv
source_embedding_size= source_embedding_size
target_embedding_size= target_embedding_size
encoding_size= encoding_size
batch_size= batch_size
learning_rate= learning_rate
num_epochs= num_epochs

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
state = torch.load("{}".format(model_path))
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
