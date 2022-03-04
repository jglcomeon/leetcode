#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：leetcode51.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/4 4:06 下午 
'''
import copy


def solveNQueens(n):
    visited_c = []
    visited_r = []
    res = []

    temp = [["." for i in range(n)] for j in range(n)]
    DFS(n, 0, 0, temp, res, visited_c, visited_r)
    return res


def DFS(n, i, j, temp, res, visited_c, visited_r):
    if i == n-1:
        if i not in visited_c and j not in visited_r:
            temp[i][j] = 'Q'
            res.append(copy.copy(temp))
            return
    if i not in visited_c and j not in visited_r:
        temp[i][j] = 'Q'
        visited_r.append(i)
        visited_c.append(j)
        DFS(i+1, 0, temp, res, visited_c, visited_r)
        temp[i][j] = '.'
        visited_r.remove(i)
        visited_c.remove(j)

    for k in range(j+1, n):
        DFS(i, j+1, temp, res, visited_c, visited_r)






if __name__ == '__main__':
    for i in range(10):
        for j in range(3):
            print(i)
            break

