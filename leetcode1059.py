'''
@Project ：leetcode 
@File    ：leetcode1059.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/10 4:51 下午 
'''
from collections import defaultdict

"""
https://cloud.tencent.com/developer/article/1787958
"""

def leadsToDestination(n, edges, source, destibation):
    graph = defaultdict(list)
    for i in edges:
        graph[i[0]].append(i[1])

    if graph[destibation]:
        return False
    visted = [False] * n
    visted[source] = True

    return DFS(graph, source, destibation, visted)


def DFS(graph, cur, destibation, visited):
    if not graph[cur] and cur != destibation:
        return False

    for next in graph[cur]:
        if visited[next]:
            return False
        visited[next] = True
        if not DFS(graph, next, destibation, visited):
            return False
        visited[next] = False
    return True


if __name__ == '__main__':
    print(leadsToDestination(3, [[0, 1], [0, 2]], 0, 2))
    print(leadsToDestination(4, [[0, 1], [0, 3],[1,2],[2,1]], 0, 3))
    print(leadsToDestination(4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3))