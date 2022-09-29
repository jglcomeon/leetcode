# pred [B,N] y = [B, N]
import numpy as np
import torch


def log_softmax(pred):
    input1 = np.exp(pred)
    loss = np.log(input1 / np.sum(input1, axis=1, keepdims=True))

    return loss


if __name__ == '__main__':
    pred = [[0.1, 0.2, 0.7], [0.62, 0.18, 0.2]]
    y = [[0, 0, 1], [0, 0, 1]]

    batch_size = 4
    class_num = 6
    inputs = torch.randn(batch_size, class_num)
    for i in range(batch_size):
        for j in range(class_num):
            inputs[i][j] = (i + 1) * (j + 1)

    print(log_softmax(inputs.numpy().tolist()))
    logsoftmax = torch.nn.LogSoftmax(dim=1)
    print(logsoftmax(inputs))


