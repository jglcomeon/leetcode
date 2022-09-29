import numpy as np
import torch


def CrossEntropyLoss(pred, y):
    input1 = np.exp(pred)
    loss = -y * np.log(input1 / input1.sum(axis=1, keepdims=True))
    print(np.sum(loss)/pred.shape[0])


if __name__ == '__main__':
    input = np.random.randn(4,3)
    y = np.array([[1,0,0],[0,0,1],[0,1,0],[0,0,1]])
    CrossEntropyLoss(input, y)

    loss = torch.nn.CrossEntropyLoss()
    print(loss(torch.tensor(input), torch.tensor([0,2,1,2])))