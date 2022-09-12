'''
@Project ：leetcode 
@File    ：huawei_test1.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/6 7:28 下午 
'''


# If you need to import additional packages or classes, please import here.
from collections import defaultdict
def func(title, text, n):
    #print(text)
    dicts = defaultdict()
    for i in text:
        if dicts.get(i, 0) == 0:
            dicts[i] = 1
        else:
            dicts[i] += int(dicts.get(i)) + 1
    for i in title:
        if dicts.get(i, 0) == 0:
            dicts[i] = 3
        else:
            dicts[i] += int(dicts.get(i)) + 3
    #print(dicts)
    dicts = sorted(dicts.items(), key=lambda x:x[1],reverse=True)
    #print(dicts)

    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().

if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    #print(m,n)
    title = []
    text = []
    text.extend()
    for i in range(m):
        title = input().split(' ')
        t = input().split(' ')
        title.extend(title)
        text.extend(t)


    print(title, text)
    func(title, text, n)
