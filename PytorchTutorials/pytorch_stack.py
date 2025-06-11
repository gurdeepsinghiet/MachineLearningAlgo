import torch

v=[[[[2, 3, 4],
          [4, 4, 4],
          [5, 5, 5]]],
          [[[2, 3, 4],
          [4, 4, 4],
          [5, 5, 5]]]]
v=torch.tensor(v)
v1=[[[[2, 3, 4],
          [4, 4, 4],
          [5, 5, 5]]],
          [[[2, 3, 4],
          [4, 4, 4],
          [5, 5, 5]]]]

v1=torch.tensor(v1)

print(v.shape)
print(v1.shape)

k=torch.stack([v,v1],dim=4)
print(k)
print(k.shape)





