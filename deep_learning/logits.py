'''
@Project ：leetcode 
@File    ：logits.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/9/8 8:22 下午 
'''

import numpy as np


class Logits:

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def initialize_params(self, dim):
        W = np.zeros((dim, 1))
        b = 0
        return W, b

    def forward(self, x, y, w, b):
        b = x.shape[0]

        z = self.sigmoid(np.dot(x, w) + b)
        loss = -1 / b * np.sum((y*np.log(z) + (1 - y) * np.log(1 - z)))
        dw = np.dot(x.T, (z - y)) / b
        db = np.sum(z - y) / b
        loss = np.squeeze(loss)
        return z, loss, dw, db

    def train(self, x, y, learn_rate, epochs):
        w, b = self.initialize_params((x.shape[0]))
        loss_list = []
        for i in range(epochs):
            z, loss, dw, db = self.forward(x, y, w, b)
            w -= dw * learn_rate
            b -= learn_rate * db
            loss_list.append(loss)
        params = {'w': w, 'b': b}
        return params