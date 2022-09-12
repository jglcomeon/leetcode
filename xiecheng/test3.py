'''
@Project ：leetcode 
@File    ：test3.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/28 7:55 下午 
'''
import sys


def test3(s):
    min1 = sys.maxsize
    n = len(s)
    for i in range(n):
        temp = 0
        for j in range(n):
            temp += min(abs(ord(s[i]) - ord(s[j])), 26 - abs(ord(s[i]) - ord(s[j])))
        if temp < min1:
            min1 = temp
    print(min1)


if __name__ == '__main__':
    s = input()
    test3(s)