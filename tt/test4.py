'''
@Project ：leetcode 
@File    ：test4.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/12 5:03 下午 
'''
from collections import Counter
"""
小美现在打音游。这个音游的玩法是这样的：

—— 共有n个房间。小美初始拥有一个指针，指在一号房间。

—— 游戏共持续m秒，每秒会有一个房间产生炸弹，小美的指针不能在这个房间中。

—— 每秒结束的瞬间，小美可以使用一次魔法，把指针切换到另一个房间中，该过程会消耗一个能量。

你的任务是计算小美无伤通过音游所需要消耗的最小能量。

保证第一秒的炸弹不发生在一号房间中。
3 10

2 3 1 3 2 1 1 2 3 1

3
"""


def test4(n, m, nums):
    cur = 1
    res = 0
    for i in range(m-1):
        if cur != nums[i+1]:
            continue
        else:
            if i+1 == m-1:
                continue
            temp = Counter(nums[i+1:])
            del temp[nums[i+1]]
            cur = list(temp.items())[-1][0]
            res += 1
    print(res)




if __name__ == '__main__':
    n, m = [int(i) for i in input().split(" ")]
    nums = [int(i) for i in input().split(" ")]
    test4(n, m, nums)

