import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


class LSTM:
    """
    Parameter
    ---------
    Wx: 输入'x'用的权重参数（整合了4个权重）
    Wh:隐藏状态'h'用的权重参数（整合了4个权重）
    b: 偏执（整合了4个偏置）
    """
    def __init__(self, Wx, Wh, b):
        self.param = [Wx, Wh, b]
        self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.cache = None

    def forward(self, x, h_prev, c_prev):
        Wx, Wh, b = self.param
        N, H = h_prev.shape
        A = np.dot(x, Wx) + np.dot(x, Wh) + b
        f = A[:, :H]
        g = A[:, H:2*H]
        i = A[:, 2*H:3*H]
        o = A[:, 3*H:]

        f = sigmoid(f)
        g = np.tanh(g)
        i = sigmoid(i)
        o = sigmoid(o)
        c_next = f * c_prev + i * g
        h_next = o * np.tanh(c_next)
        return h_next, c_next



