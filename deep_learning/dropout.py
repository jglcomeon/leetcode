import numpy as np


class Dropout:
    def __init__(self, drop_rate=0.5):
        self.drop_rate = drop_rate
        self.mask = None

    def forward(self, x, is_train=True):
        if is_train:
            self.mask = np.random.rand(*x.shape) > self.drop_rate
            return x * self.mask
        else:
            return x * (1.0 - self.drop_rate)

    def backward(self, dout):
        return dout * self.mask


if __name__ == '__main__':
    dropout = Dropout()
    x = np.array([1,1,1,1,1,1,1,1,1,1])
    print(dropout.forward(x))