#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：Union-Find.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/2/28 5:04 下午 
'''

class Union_Find:

    def __init__(self, n):
        self.father = [0] * n
        for i in range(n):
            self.father[i] = i

    def find(self, x):
        if self.father[x] == x:
            return x
        else:
            return self.find(self.father[x])

    def merge(self, i, j):

        self.father[self.find(i)] = self.find(j)


def findCircleNum(friends):
    n = len(friends)
    u = Union_Find(n)
    for i in range(n):
        for j in range(len(friends[0])):
            if i != j and friends[i][j] == 1:
                u.merge(j, i)
    res = set()
    for i in range(n):
        if u.find(i) == i:
            res.add(i)
    return len(res)


if __name__ == '__main__':
    print(findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

