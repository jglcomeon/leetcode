#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：leetcode547.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/2/28 4:33 下午 
'''


def findCircleNum(friends):
    visited = [False for j in range(len(friends))]
    res = 0
    for i in range(len(friends)):
        if not visited[i]:
            DFS(friends, i, visited)
            res += 1
    return res


def DFS(friends, i, visited):
    visited[i] = True
    for j in range(len(friends)):
        if not visited[j] and friends[i][j] == 1:
            DFS(friends, j, visited)


if __name__ == '__main__':
    print(findCircleNum([[1,1,0], [1,1,0], [0,0,1]]))