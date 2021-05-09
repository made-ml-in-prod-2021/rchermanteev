import torch
import torch.nn as nn
import torch.nn.functional as F


class SimpleNet(nn.Module):
    def __init__(self, in_count, output_count):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(in_count, 32)
        self.fc2 = nn.Linear(32, 32)
        self.fc3 = nn.Linear(32, output_count)

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return F.relu(x)

    def fit(self):
        pass

    def predict(self):
        pass
