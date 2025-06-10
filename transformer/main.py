import torch
import torch.nn as nn
import numpy as np


text="the Animal didn't cross the street because it was too tired"
words=text.lower().split(" ")
unique_elements, indices = np.unique(words, return_index=True)
print(unique_elements,indices)
print(np.argsort(indices))
vocab=unique_elements[np.argsort(indices)]
print(vocab)


vk=nn.Embedding(10,512)
print(vk)

def word_to_index(vocab):
    w_t_i={w: i for i,w in enumerate(vocab)}
    return w_t_i

w_t_i=word_to_index(vocab)
print(w_t_i)

encoded_sentence=[w_t_i[word] for word in words]
print(encoded_sentence)

w_emb=vk(torch.LongTensor(encoded_sentence))
print(w_emb)










