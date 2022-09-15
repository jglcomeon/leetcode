'''
@Project ：leetcode 
@File    ：leetcode1135.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/10 5:27 下午 
'''
class Union:
    def __init__(self, n):
        self.farther = [i for i in range(n+1)]

    def find(self, x):
        if x == self.farther[x]:
            return x
        return self.find(self.farther[x])

    def merge(self, i, j):
        a = self.find(i)
        b = self.find(j)
        self.farther[a] = b

def minimumCost(N, connections):
    union = Union(N)
    connections = sorted(connections, key=lambda x: x[-1])
    res = 0
    edges = 0
    for i in connections:
        a = i[0]
        b = i[1]
        cost = i[2]
        if union.find(a) != union.find(b):
            union.merge(a, b)
            res += cost
            edges += 1
        if edges == N-1:
            break

    if edges == N - 1:
        return res
    return -1


if __name__ == '__main__':
    print(minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]]))
    print(minimumCost(4, [[1,2,3],[3,4,4]]))


