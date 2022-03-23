'''
@Project ：leetcode 
@File    ：pdd_test1.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/20 7:04 下午 
'''

def test(n, a, b):
        res = 0
    a = sorted(a)
    b = sorted(b)
    for i in range(n):
        res += (a[i] - b[i]) **2

    print(res)


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().strip().split(' ')]
    b = [int(i) for i in input().strip().split(' ')]
    test(n, a, b)

