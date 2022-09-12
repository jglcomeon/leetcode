'''
@Project ：leetcode 
@File    ：leetcode127.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/7 9:30 上午 
'''
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0

        #dicts = defaultdict(list)

        n = len(beginWord)

        queen = deque()
        queen.append(beginWord)
        level = 1
        visited = set()
        visited.add(beginWord)
        chars = [chr(i) for i in range(97,123)]

        while queen:


            q_l = len(queen)

            for t_i in range(q_l):
                q = queen.popleft()
                word_l = list(q)
                for i in range(n):
                    origin = word_l[i]
                    for j in chars:
                        word_l[i] = j

                        t_q = "".join(word_l)
                        if t_q in wordList:
                            if t_q == endWord:
                                return level + 1
                            if t_q not in visited:
                                queen.append(t_q)
                                visited.add(t_q)
                    word_l[i] = origin
            level += 1
        return 0

if __name__ == '__main__':
    s = Solution()
    s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])

