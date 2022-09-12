'''
@Project ：leetcode 
@File    ：al_test3.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/23 10:04 下午 
'''

def test4(n, m):
    dp = [[1 if i == 0 else 0 for j in range(m+1)] for i in range(n+1)]

    mod = 1000000007
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(i):
                dp[i][j] = (dp[i][j] + dp[k][j-1] * dp[i-1-k][j-1]%mod) % mod
    print(dp[n][m])

if __name__ == '__main__':
    n, m = [int(i) for i in input().split(' ')]
    test4(n, m)