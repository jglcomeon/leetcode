'''
@Project ：leetcode 
@File    ：demo1.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/8/7 7:43 下午 
'''
from collections import Counter
def demo1(s, n, words):
    dicts = Counter(s)
    res = -100
    for i in range(n):
        w = words[i]
        temp_m = int('inf')
        count_w = Counter(w)
        for j in count_w:
            temp_m = min(dicts[j] // count_w[j], temp_m)
        res = max(res, temp_m)
    print(res)




if __name__ == '__main__':
    M = int(input())
    for i in range(M):
        s = input()
        n = int(input())
        words = input().split(' ')
        demo1(s, n, words)