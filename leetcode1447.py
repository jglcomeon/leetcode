#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：leetcode1447.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/2/11 7:26 下午 
'''
class Solution:

    def simplifiedFractions(self, n):
        res = []
        for i in range(2, n+1):
            for j in range(1, i):
                if self.gcd(i, j) == 1:
                    res.append("{}/{}".format(j, i))
        return res

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return a * b / self.gcd(a, b)


if __name__ == '__main__':
    s = Solution()
    print(s.simplifiedFractions(6))

