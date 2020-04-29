import torch
import numpy as np
import matplotlib.pyplot as plt
from torch import nn,optim
from mpl_toolkits.mplot3d import Axes3D
from torch.utils.data import Dataset, DataLoader


z = torch.tensor([[2,5,0],[10,8,2],[6,5,1]])
_, yhat = z.max(1)

print(yhat)
