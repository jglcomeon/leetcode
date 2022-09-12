'''
@Project ：leetcode 
@File    ：leetcode713.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/5/6 8:34 上午 
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums, k) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            sum_d = nums[i]
            index = i - 1
            if sum_d < k:
                res += 1
            while sum_d < k and index >= 0:

                sum_d *= nums[index]
                if sum_d < k:
                    res += 1
                index -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    s.numSubarrayProductLessThanK([10,5,2,6], 100)
