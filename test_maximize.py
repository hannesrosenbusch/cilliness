from maximize import maximum
import torch

def test_maximum():
	t = torch.tensor([[4., -1.], [3., -3.]])
	assert torch.max(t) == torch.tensor(4.)
