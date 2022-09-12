'''
@Project ：leetcode 
@File    ：demo2.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/9/2 5:30 下午 
'''

n, p = input().split(' ')

n = int(n)
p = 1 - float(p)
i = 0
fenzi = 1
fenmu = 1
while i<=n:
    fenzi *= (n - i)
    fenmu *= n
    r = round(fenzi / fenmu, 8)
    if abs(r - p) <= 0.009:
        print(i+1)
        break
    i += 1
