'''
@Project ：leetcode 
@File    ：test2.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/28 7:38 下午 
'''

def test2(n, m, a, b):
    res = 0
    if a > b:
        temp_a = n // 2
        if m > temp_a:
            res += temp_a * a
            n -= temp_a * 2
            m -= temp_a
        else:
            res += m * a
        if n > 0 and m >= 2:
            res += b
    else:
        temp_b = m // 2
        if n > temp_b:
            res += temp_b * b
            m -= temp_b * 2
            n -= temp_b
        else:
            res += n * b
        if m > 0 and n >=2:
            res += a
    print(res)


if __name__ == '__main__':
    n, m, a, b = map(int, input().split(' '))
    test2(n, m, a, b)