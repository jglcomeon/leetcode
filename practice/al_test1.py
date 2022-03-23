'''
@Project ：leetcode 
@File    ：al_test1.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/21 11:25 下午 
'''


def test(X, Y, n):
    nums = sorted(zip(X, Y), key=lambda x: (x[0], -x[1]))
    new_nums = [i[1] for i in nums]
    res = -10000
    dp = [1] * n
    for i in range(1, n):
        j = i - 1
        while j >= 0:
            if new_nums[i] > new_nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
                res = max(res, dp[i])
            j -= 1
    return res


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        X = [int(j) for j in input().split(' ')]
        Y = [int(j) for j in input().split(' ')]
        print(test(X, Y, n))
