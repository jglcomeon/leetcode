import copy


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int):
        if n == 1:
            return [['Q']]
        if n <= 3:
            return []
        dp = [['Q' for i in range(n)] for j in range(n)]
        res = []

        def shade(dp, row, column):
            for i in range(n):
                if i != column:
                    dp[row][i] = '.'
                if i != row:
                    dp[i][column] = '.'

            index_i = row + 1
            index_j = column + 1
            while index_i < n and index_j < n:
                dp[index_i][index_j] = '.'
                index_i += 1
                index_j += 1
            index_i = row + 1
            index_j = column - 1
            while index_i < n and index_j >= 0:
                dp[index_i][index_j] = '.'
                index_i += 1
                index_j -= 1

        def DFS(dp, row):

            if row == n - 1:

                for i in range(n):
                    if dp[n - 1][i] == 'Q':
                        self.res.append(["".join(i) for i in dp])
                return

            for i in range(n):
                if dp[row][i] == 'Q':
                    temp = copy.deepcopy(dp)
                    shade(dp, row, i)
                    DFS(dp, row + 1)
                    dp = temp

        DFS(dp, 0)
        return self.res
