import torch
import torch.nn as nn


class inputEmbedding(nn.Module):

    def __init__(self,d_model:int,vocab:int):
        super.__init__()
        self.d_model=d_model
        self.vocab=vocab
        self.embeddings=nn.Embedding(10,512)