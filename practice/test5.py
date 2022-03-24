#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：test5.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/24 8:17 下午 
'''

def test5(nums, n):
    m = []
    nums = sorted(nums, key=lambda x: abs(x[0]-x[1]))
    maxa = nums[0][0]
    maxb = nums[0][1]
    res = 0
    for a,b in nums:
        if a > b:
            res = max(res, (maxb + b)/2)
        else:
            res = max(res, (maxa + a)/2)
        if a > maxa:
            maxa = a
        if b > maxb:
            maxb = b
    return res


if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        nums.append([int(i) for i in input().split(' ')])
    print(test5(nums, n))
