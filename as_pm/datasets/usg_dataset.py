import json
import os

import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset


class USG_Dataset(Dataset):
    def __init__(
        self,
        root: str,
        seed: int = 42,
        mode: str = "train",
        test_ratio: float = 0.1,
        val_ratio: float = 0.2,
    ):
        self.root = root
        self.seed = seed
        self.mode = mode
        self.test_ratio = test_ratio
        self.val_ratio = val_ratio

        self.samples = []
        for filename in os.listdir(self.root):
            self.samples.append(f"{self.root}/{filename}")

    def to_tensor(self, x):
        return torch.tensor(x, dtype=torch.float32)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path = self.samples[idx]
        with open(path, "r") as json_file:
            x = json.load(json_file)
            label = json.load(json_file)
        return self.to_tensor(x), self.to_tensor(label)
