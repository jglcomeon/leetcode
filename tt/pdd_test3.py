'''
@Project ：leetcode 
@File    ：pdd_test3.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/20 7:33 下午 
'''

def test3(k ,b):
    len1 = len(b)
    a = ['1'] * len1
    visited = [False] * len1
    for i in range(len1):
        if b[i] == 0:
            if i >= k:
                a[i-k] = '0'
            if i + k < len1:
                a[i+k] = '0'


    print(" ".join(a))


if __name__ == '__main__':
    k = int(input())
    b = [int(i) for i in input().strip()]
    test3(k,  b)