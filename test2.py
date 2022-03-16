'''
@Project ：leetcode 
@File    ：test2.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/12 4:40 下午 
'''

"""
小美现在在厨房做饭。小美发现食材现在只够每种菜做一份。

现在同一时刻（即不分先后顺序）来了n个顾客。每个顾客都有想两份要点的菜。只有当顾客吃到全部自己想要的菜的时候，顾客才会满意。

现在你的任务是，合理地接取顾客的订单要求，尽可能让更多的顾客满意，并输出最多有多少顾客可以满意。
3 4
1 2
2 3
3 4

2
"""
def test2(n, m, nums):
    res = 1
    nums = sorted(nums)
    n = len(nums)
    j = 1
    while j < n:
        if nums[j][0] == nums[j-1][1] or (j+1 < n and nums[j][1] == nums[j+1][0]):
            nums.remove(nums[j])
            n = len(nums)
        else:
            res += 1
            j += 1
    print(res)


if __name__ == '__main__':
    n, m = [int(i) for i in input().split(" ")]
    t = n
    nums = []
    while t >= 1:
        nums.append([int(i) for i in input().split(" ")])
        t -= 1
    test2(n, m, nums)
