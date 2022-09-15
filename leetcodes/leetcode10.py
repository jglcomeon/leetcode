#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：leetcode10.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/2/22 2:33 下午 
'''

# "mississippi"
# "mis*is*p*."
def isMatch(s, p):

    len1 = len(s)
    len2 = len(p)
    dp = [[False for i in range(len2+1)] for j in range(len1+1)]
    dp[0][0] = True
    for i in range(1, len2+1):
        if p[i-1] == '*':
            dp[0][i] = dp[0][i-2]

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if p[j-1] == '.' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i-1][j] | dp[i][j-2]

    return dp[len1][len2]




