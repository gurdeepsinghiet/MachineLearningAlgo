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


    def positional_encoding(self,sentence_seq):
        l=len(sentence_seq)
        pe=torch.zeros(l,self.d_model)
        even_i=torch.arange(0,self.d_model,2)
        odd_i=torch.arange(1,self.d_model,2)
        even_denominator=torch.pow(10000,even_i/self.d_model)
        odd_denominator=torch.pow(10000,odd_i/self.d_model)
        pos=torch.arange(l,dtype=torch.float)
        pos=pos.reshape(l,1)
        denominator=even_denominator
        even_PE=torch.sin(pos/denominator)
        odd_PE=torch.cos(pos/denominator)






