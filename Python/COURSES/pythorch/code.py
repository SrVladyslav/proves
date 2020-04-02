import torch

'''
a = torch.tensor([10,9,8,7])
print(a[1:3])

u=torch.tensor([1,2])
v=torch.tensor([0,1])
print(torch.dot(u,v))
'''
a=torch.linspace(1, 3, steps=5)
print(a.mean())
print(a)