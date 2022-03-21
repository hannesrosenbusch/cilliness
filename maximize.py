'''trying out some CI silliness'''
import torch

def maximum(my_tensor):
    '''takes tensor, returns max of tensor'''
    return torch.max(my_tensor)

t = torch.Tensor([[4., -1.], [3., -3.]])
print(maximum(t))
