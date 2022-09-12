
class Solution:
    def maxScore(self, energy: int, actions) -> int:
        dp = [0 for i in range(energy+1)]
        n = len(actions)
        for i in range(n):
            n = actions[i][0]
            m = actions[i][1]
            for j in reversed(range(n, energy+1)):
                dp[j] = max(dp[j], dp[j-n] + m)
        print(dp[energy])
        return dp[energy]

s = Solution()
s.maxScore(10,[[1,1],[2,3],[3,5],[5,10],[7,9],[8,10]])


