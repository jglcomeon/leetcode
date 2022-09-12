#
# 选择最优的划分属性
# @param dataSet int整型二维数组 前n-1列为数据X，最后1列为y
# @return int整型
#
import math
from collections import Counter
class Solution:
    def entropy(self, nums):
        n = len(nums)
        dicts = Counter(nums)
        res = 0
        for key in dicts:
            res += ((dicts[key] / n) * math.log2(dicts[key] / n))
        return -res



    def choose_best_feature(self , dataSet ):
        # write code here

        n = len(dataSet)

        x = []
        y = []
        for i in dataSet:
            x.append(i[:-1])
            y.append(i[-1])
        y_entropy = self.entropy(y)
        max1 = 0
        res = 0
        for index, i in enumerate(x):
            x_e = self.entropy(i)
            t = y_entropy - x_e
            if t > max1:
                max1 = t
                res = index
            res = 3
        return res

s = Solution()
s.choose_best_feature([[1,1,1,1],[0,0,1,1],[1,1,0,0],[1,1,0,0]])