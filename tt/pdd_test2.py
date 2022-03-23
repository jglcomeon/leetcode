'''
@Project ：leetcode 
@File    ：pdd_test2.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/20 8:35 下午 
'''
"""

1
2 3
5 1 2
3 2 3

"""


def test(v, dicts1, dicts2, max_day):
    res = 0
    dicts1 = sorted(dicts1.items(), key=lambda x:x[1])
    for i in range(max_day-1):
        temp = v
        while temp > 0 and dicts1:
            for t in range(len(dicts1)):
                if dicts1[t][1][0] <= i+1 <= dicts1[t][1][1]:
                    if dicts2[dicts1[t][0]] <= temp:
                        res += dicts2[dicts1[t][0]]
                        dicts2[dicts1[t][0]] = 0
                        temp -= dicts2[dicts1[t][0]]
                    else:
                        res += temp

                        dicts2[dicts1[t][0]] -= temp
                        temp = 0
                if dicts2[dicts1[t][0]] == 0:
                    dicts2.remove(dicts1[t][0])
                    dicts1.pop(t)

                if temp:
                    break

    return res


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, v = [int(j) for j in input().split(' ')]
        nums = []
        max_day = -1000000
        dicts1 = {}
        dicts2 = {}
        for x in range(n):
            ki, ai, bi = [int(j) for j in input().split(' ')]
            max_day = max(max_day, bi)
            dicts1[x] = [ai, bi]
            dicts2[x] = ki

        print(test(v, dicts1, dicts2, max_day))
