'''
@Project ：leetcode 
@File    ：huawei_test2.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/6 7:57 下午 
'''

def test(dicts, target):
    if dicts.get(target, "") == "":
        return -1
    queen = [target]
    visited = []
    path = []
    level = 0
    while queen:
        t = queen.pop()
        visited.append(str(t))
        path.append(t)

        if dicts.get(t, "") != "":
            for d in dicts[t]:

                if d in path:
                    print(-1)
                    return

                queen.append(d)
        else:
            break
    print(",".join(sorted(reversed(visited[1:]))))


if __name__ == '__main__':
    N = int(input())
    target = int(input())
    dicts = {}
    for i in range(N):
        s = input()
        if s == '0':
           continue
        else:
            s = s.split(',')[1:]
            dicts[i] = [int(j) for j in s]
    test(dicts, target)
