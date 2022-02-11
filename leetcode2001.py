#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：leetcode2001.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/2/11 10:49 上午 
'''
from collections import defaultdict


class Solution:
    def gridIllumination(self, n, lamps, queries):
        point = set()
        rows = defaultdict()
        columns = defaultdict()
        diagonal = defaultdict()
        antiDiagonal = defaultdict()
        res = []
        for r, c in lamps:
            if (r, c) in point:
                continue
            point.add((r, c))
            rows[r] = rows.get(r, 0) + 1
            columns[c] = rows.get(c, 0) + 1
            diagonal[r-c] = diagonal.get(r-c, 0) + 1
            antiDiagonal[r+c] = antiDiagonal.get(r+c, 0) + 1
        for r, c in queries:
            if rows[r] or columns[c] or diagonal[r-c] or antiDiagonal[r+c]:
                res.append(1)
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if (i, j) not in point or i < 0 or j < 0 or i >= n or j >= n:
                        continue
                    point.remove((i, j))
                    rows[i] -= 1
                    columns[j] -= 1
                    diagonal[i - j] -= 1
                    antiDiagonal[i + j] -= 1


