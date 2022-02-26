'''
@Project ：leetcode 
@File    ：a_N.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/2/25 7:56 下午 
'''


def a_n(a, b):
    if b == 1:
        return a
    if b % 2 == 0:
        return a_n(a,b//2) * a_n(a, b//2)
    else:
        return a_n(a,b-1) * a

if __name__ == '__main__':
    print(a_n(5,5))