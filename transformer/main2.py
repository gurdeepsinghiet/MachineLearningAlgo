from collections import Counter
import torch
import torch.nn as nn
# This is going to be the dummy sentence :
sentences = "this is the second example showing for the article at gfg. and doing this is actually really fun"

words = sentences.split(' ')

# create a dictionary
vocab = Counter(words)
print(vocab.get)
vocab = sorted(vocab, key=vocab.get, reverse=True)
print("=============")
print(vocab)
vocab_size = len(vocab)

# create a word to index dictionary from our Vocab dictionary
word2idx = {word: ind for ind, word in enumerate(vocab)}
print(word2idx)
encoded_sentences = [word2idx[word] for word in words]
print(encoded_sentences)
e_dim = 5
emb = nn.Embedding(vocab_size, e_dim, padding_idx = 3)
word_vectors = emb(torch.LongTensor(encoded_sentences))

#print the word_vectors
print(word_vectors)

