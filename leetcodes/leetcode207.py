from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        dicts = defaultdict(list)
        dicts2 = defaultdict(list)

        for i, j in prerequisites:
            dicts[i].append(j)
            dicts2[j].append(i)
        
        res = set()
        nums = [i for i in range(numCourses)]
        while 1:
            flag = False
            for i in nums:
                if dicts[i] == []:
                    flag = True
                    res.add(i)
                    nums.remove(i)
                    for j in dicts2[i]:
                        dicts[j].remove(i)
            if not flag:
                break
             

        if len(res) == numCourses:
            return True
        return False

            

        
