'''
@Project ：leetcode 
@File    ：test1.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/12 4:19 下午 
'''
def test(nums):
    n = len(nums)
    # dp = [[1 if i == 1 and nums[i] == 1 else 0 for i in range(n)] for j in range(n)]
    # for i in range(n):
    #     j = i - 1
    #     while j >= 0:
    #         if nums[i] * nums[j] == 1:
    #             if i - j == 1:
    #                 dp[j][i] = 1
    #             dp[j][i] = dp[j+1][i-1]
    #         j -= 1
    # res = 0
    # for d in dp:
    #     res += sum(d)
    # print(res)
    res = 0
    for i in range(n):
        if nums[i] == 1:
            res += 1
        j = i + 1
        temp = nums[i]
        while j < n:
            temp *= nums[j]
            if temp > 0:
                res += 1
            j += 1
    print(res)


if __name__ == '__main__':
    n = int(input().strip())
    nums = input().split(" ")
    nums = [int(i) for i in nums]

    test(nums)