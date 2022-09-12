'''
@Project ：leetcode 
@File    ：demo2.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/8/6 10:41 上午 
'''
import sys


def test2(nums, n):
    dp1 = [0 for i in range(n)]
    dp2 = [0 for i in range(n)]

    x, y = 0, 0
    for i in range(n):
        if nums[i] >=0:
            x += 1
        dp1[i] = x

    for i in reversed(range(n)):
        if nums[i] <= 0:
            y += 1
        dp2[i] = y
    res = sys.maxsize
    for i in range(n):
        res = min(res, dp1[i] + dp2[i] - 1)
    print(res)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split(' ')))
    test2(nums, n)