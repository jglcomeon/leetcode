"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

"""

class Solution:

    def numIslands(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        visited = [[False for i in range(n)] for j in range(m)]

        def dfs(grid, visited, i, j):

            visited[i][j] = True
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for t_i, t_j in direction:
                cur_i = t_i + i
                cur_j = t_j + j
                if cur_i >= 0 and cur_i < m and cur_j >= 0 and cur_j < n and not visited[cur_i][cur_j] and grid[cur_i][cur_j] == '1':
                    dfs(grid, visited, cur_i, cur_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, visited, i, j)
                    res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(s.numIslands(grid))
    grid2 = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
    ]
    print(s.numIslands(grid2))


