import torch
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

abcd_padded = torch.tensor([1,2,3,4], dtype=torch.float32)
efg_padded = torch.tensor([5,6,7,0], dtype=torch.float32)
h_padded = torch.tensor([8,0,0,0], dtype=torch.float32)

padded_tensor = torch.stack([abcd_padded, efg_padded, h_padded])
lengths = [4,3,1]

print(padded_tensor) # shape (3,4)
print(padded_tensor.shape)
print(lengths)

packed_tensor = pack_padded_sequence(padded_tensor, lengths, batch_first=True)
print(packed_tensor)

unpacked_tensor, unpacked_lengths = pad_packed_sequence(packed_tensor, batch_first=True)

print("-----")
print(unpacked_tensor)
print(unpacked_lengths)


