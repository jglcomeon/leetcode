'''
@Project ：leetcode 
@File    ：test2.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/24 8:40 下午 
'''

def test2(vector_c, matrix):
    res = []

    n = len(vector_c)
    for i in range(n):
        temp_sum = 0
        for j in range(n):
            temp_sum += vector_c[j] * matrix[j][i]
        res.append(temp_sum)

    maxs = max(res)
    print(res.index(maxs))


if __name__ == '__main__':
    c = int(input())
    vector_c = list(map(float, input().split(' ')))
    matrix = []
    for i in range(c):
        temp = list(map(float, input().split(' ')))
        matrix.append(temp)
    test2(vector_c, matrix)
