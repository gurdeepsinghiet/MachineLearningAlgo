import torch
import torch.nn as nn


b=nn.Embedding(10,512)
print(b)

torch.manual_seed(100)
x=torch.randn(2,3)
print(x)

print(x.sum())

class inputEmbedding(nn.Module):

    def __init__(self,d_model:int,vocab:int):
        super.__init__()
        self.d_model=d_model
        self.vocab=vocab
        self.embeddings=nn.Embedding(10,512)


    def forward(self,word_seq):
        self.embeddings(word_seq)
