'''
@Project ：leetcode 
@File    ：leetcode213.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/2/26 11:59 上午 
'''

class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        dp = [0 for i in range(n)]
        dp1 = [0 for i in range(n)]
        dp[1] = nums[0]
        dp1[1] = nums[1]

        for i in range(2, n):

            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])

        return max(dp[n-1],dp1[n-1])

if __name__ == '__main__':
    s = Solution()
    s.rob([1,2,1,1])