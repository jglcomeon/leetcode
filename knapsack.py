# 0-1背包问题 每个物品只能拿0次或者1次
def knapsack_0_1(weights, values, N, W):
    dp = [[0 for i in range(W)] for j in range(N)]
    for i in range(1, N+1):
        w = weights[i-1]
        v = values[i-1]
        for j in range(1, W+1):
            if j >= w:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[N][W]


def knapsack_0_1_2(weights, values, N, W):
    dp = [0 for i in range(W+1)]
    for i in range(1, N+1):
        w = weights[i-1]
        v = values[i-1]
        for j in reversed(range(w, W)):
            dp[j] = max(dp[j], dp[j-w] + v)
    return dp[W]


# 完全背包问题 每个物品可以拿多次
def knapsack_0_1_complete(weights, values, N, W):
    dp = [[0 for i in range(W)] for j in range(N)]
    for i in range(1, N+1):
        w = weights[i-1]
        v = values[i-1]
        for j in range(1, W+1):
            if j >= w:
                dp[i][j] = max(dp[i-1][j], dp[i][j-w] + v)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[N][W]
