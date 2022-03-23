#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：al_test2.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/23 12:50 下午 
'''
from math import sqrt


def test2(A, B, n):
    mod = 1e9+7
    a, b, c = A, (A**2 - B*2) % mod, 0
    if n == 1:
        return A
    if n == 2:
        return b
    while n > 2:
        c = (A * b - B*a) % mod
        a = b
        b = c
        n -= 1
    return c

def test3(A, B, n):
    mod = 1e9 + 7
    a = sqrt(A**2-4*B)
    x = (a + A) // 2
    y = A - x
    return (x**n + y**n) % mod


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        A, B, n = [int(j) for j in input().split(' ')]
        print(test2(A, B, n))