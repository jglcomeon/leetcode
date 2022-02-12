class Solution:
    def checkValid(self, matrix) -> bool:
        n = len(matrix)
        target = list(range(1, n+1))
        for i in range(n):
            temp1 = sorted(matrix[i])
            if temp1 != target:
                return False
            temp = []
            t = 0
            while t < n:
                temp.append(matrix[t][i])
                t += 1
            if sorted(temp) != target:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.checkValid([[1,2,3],[3,1,2],[2,3,1]]))