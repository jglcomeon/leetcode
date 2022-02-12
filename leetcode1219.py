import copy


class Solution:

    def getMaximumGold(self, grid) -> int:
        row = len(grid)
        max_1 = 0
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                visited = [[False for i in range(column)] for i in range(row)]
                max_1 = max(max_1, self.DFS(i, j, grid, visited))
        return max_1

    def DFS(self, i, j, grid, visited):
        if grid[i][j] == 0 or visited[i][j]:
            return 0
        direction = [[0, 1],[0, -1], [1, 0], [-1, 0]]
        visited[i][j] = True
        temp_max = 0
        for d_i, d_j in direction:
            temp_i = i + d_i
            temp_j = j + d_j
            if temp_i >= 0 and temp_i < len(grid) and temp_j >= 0 and  temp_j < len(grid[0]) and not visited[temp_i][temp_j] and grid[temp_i][temp_j]!=0:
                print("ddd")
                temp_max = max(temp_max, self.DFS(temp_i, temp_j, grid, visited))
                visited[temp_i][temp_j]=False
        return temp_max + grid[i][j]


if __name__ == '__main__':
    s = Solution()
    s.getMaximumGold([[0,0,0,0,0,0,32,0,0,20],[0,0,2,0,0,0,0,40,0,32],[13,20,36,0,0,0,20,0,0,0],[0,31,27,0,19,0,0,25,18,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,18,0,6],[0,0,0,25,0,0,0,0,0,0],[0,0,0,21,0,30,0,0,0,0],[19,10,0,0,34,0,2,0,0,27],[0,0,0,0,0,34,0,0,0,0]])