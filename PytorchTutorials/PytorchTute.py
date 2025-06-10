import torch
import torch.nn as nn
import numpy as np

a=torch.tensor([[1,1,1]])
print(a.shape)

ad0=torch.squeeze(a,dim=0)
print(ad0.shape)
print(ad0)
#text