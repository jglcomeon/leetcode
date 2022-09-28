#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
from sortedcontainers import SortedDict
from collections import defaultdict
class Solution:
    def changeNumber(self, n: int) -> int:
        # write code here

        #         visited = [False for i in range(n)]
        nums = list(str(n))
        l = len(nums)
        for i in range(l):
            if i % 2 == 0:
                if i == 0:
                    if nums[i] != '1':
                        nums[i] = '1'
                    else:
                        nums[i] = '2'
                else:
                    if nums[i] != '0':
                        nums[i] = '0'
                    else:
                        nums[i] = '1'
            else:
                if nums[i] != '9':
                    nums[i] = '9'
                else:
                    nums[i] = '8'
        return int("".join(nums))

s = Solution()
s.changeNumber(191)
