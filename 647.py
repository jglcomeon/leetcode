class Solution:
    def countSubstrings(self, s: str) -> int:
        len1 = len(s)
        if len1 < 1:
            return len1
        dp = [[1 if i== j else 0 for i in range(len1)] for j in range(len1)]
        for i in range(len1):
            j = i - 1
            while j >=0:
                if s[i] == s[j]:

                    if i-j <=2:
                        print(i)
                        dp[j][i] = 1
                    else:
                        dp[j][i] = dp[j+1][i-1]
                j -= 1
        res = 0
        print(dp)
        for d in dp:
            res += sum(d)
        return res
