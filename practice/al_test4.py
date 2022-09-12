#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：al_test4.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/30 5:19 下午 
'''


def test4(dp, n, m):
    si, sj = 0, 0
    is_found = False
    for i in range(n):
        for j in range(m):
            if dp[i][j] == 'S':
                si, sj = i, j
                is_found = True
                break
        if is_found:
            break
    deque = [(si, sj, 5, 0)]
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    step = 0
    dp[si][sj] = '#'
    while deque:
        i, j, p, step = deque.pop(0)
        if dp[i][j] == 'E':
            break
        dp[i][j] = '#'
        for ti, tj in directions:
            temp_i = ti + i
            temp_j = tj + j
            if temp_i >= 0 and temp_i < n and temp_j >=0 and temp_j < m and dp[temp_j][temp_j] != '#':
                deque.append((temp_i, temp_j, p, step+1))
        if n-1 - i >= 0 and m -1- j >=0 and dp[n-1-i][m-1-j] != '#' and p>=0:
            deque.append((n-1-i, m-1-j, p-1, step+1))
    print(step)



if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    dp = []
    for i in range(n):
        dp.append([i for i in input().strip()])
    test4(dp, n, m)
    print(dp)