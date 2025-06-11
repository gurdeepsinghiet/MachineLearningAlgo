import torch


x1=torch.tensor([[1,1,1],
                [2,2,2]])

x2=torch.tensor([[3,3,3],
                [4,4,4]])

us=x1.unsqueeze(dim=1)
print(us.shape)
print(us)
sdim0=torch.stack([x1,x2],dim=2)
print(sdim0)
print(sdim0.shape)


x3=[[[2,3,4],
     [4,4,4],
     [5,5,5]],
    [[2, 3, 4],
     [4, 4, 4],
     [5, 5, 5]]
    ]




x3=torch.tensor(x3)
print(x3.unsqueeze(dim=1))
print(x3.unsqueeze(dim=1).shape)

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

v=torch.reshape(v,[2,1,3,3])
print(v)


