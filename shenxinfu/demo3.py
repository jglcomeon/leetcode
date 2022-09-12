'''
@Project ：leetcode 
@File    ：demo3.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/9/1 8:27 下午 
'''


dicts = {'o': '0', 'y': '1', 'e':'2', 'a':'3', 's':'4'}
re_dict = {}
for k, v in dicts.items():
    re_dict[v] = k
T = int(input())
for i in range(T):
    a = input().strip()
    s = ""
    is_five = False
    for j in a:
        if dicts.get(j, '') != '':
            s += dicts[j]
            is_five = True
        else:
            s += j
    if is_five:
        print(int(s, base=5))
    else:
        s = int(s)
        res = []
        while s:
            res.append(str(s % 5))
            s //= 5

        f_s = []
        for ttt in reversed(res):
            f_s.append(re_dict[ttt])
        print("".join(f_s))




