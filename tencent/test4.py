'''
@Project ：leetcode 
@File    ：test4.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/24 9:12 下午 
'''


def test4(ai, bi, matrix, q):
    ai.sort()
    bi.sort()
    res = [0] * 3
    for i in matrix:
        l, r = i[0], i[1]
        red = 0
        blue = 0
        for j in ai:
            if l <= j <= r:
               red += 1

            if j > r:
                break
        for j in bi:
            if l <= j <= r:
                blue += 1

            if j > r:
                break

        if red > blue:
            res[0] += 1
        elif red == blue:
            res[1] += 1
        else:
            res[2] += 1
    print(' '.join([str(i) for i in res]))



if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    ai = list(map(int, input().split(' ')))
    bi = list(map(int, input().split(' ')))
    q = int(input())
    matrix = []
    for i in range(q):
        matrix.append(list(map(int, input().split(' '))))
    test4(ai, bi, matrix, q)

