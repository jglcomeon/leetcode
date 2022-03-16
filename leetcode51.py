import copy


class Solution:
    def __init__(self):
        self.res = []
    def solveNQueens(self, n) :
        if n == 1:
            return [["Q"]]
        if n > 1 and n < 4:
            return []
        dp = [['Q' for i in range(n)] for j in range(n)]
        re = []
        self.DFS(n, dp, 0)
        for ar in self.res:
            temp = []
            for i in ar:
                temp.append("".join(i))
            re.append(temp)

        return re

    def DFS(self, n, dp, row):
        if row == n - 1:
            for i in range(n):
                if dp[row][i] == 'Q':
                    self.res.append(copy.copy(dp))
            return
        for i in range(n):
            if dp[row][i] == 'Q':
                temp = copy.deepcopy(dp)
                self.shade(n, dp, row, i)
                self.DFS(n, dp, row + 1)
                dp = temp

    def shade(self, n, dp, row, column):

        for i in range(n):
            dp[i][column] = '.'
            dp[row][i] = '.'
        i_1, j_1 = row + 1, column - 1
        while i_1 < n and j_1 >= 0:
            dp[i_1][j_1] = '.'
            i_1 += 1
            j_1 -= 1
        i_2, j_2 = row + 1, column + 1
        while i_2 < n and j_2 < n:
            dp[i_2][j_2] = '.'
            i_2 += 1
            j_2 += 1
        dp[row][column] = 'Q'