#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 找出并返回满足条件且不重复的三元组
# @param nums int整型一维数组 包含n个整数的数组nums
# @param target int整型 目标值
# @return int整型二维数组
#
class Solution:
    def threeSum(self , nums, target: int):
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        i = 0
        result = []
        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if res == target:
                    result.append((nums[i], nums[left], nums[right]))
                    while left > right and nums[right] == nums[right-1]:
                        right -= 1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    right -= 1
                elif res > target:
                    while left < right and nums[right] == nums[right-1]:right=right-1
                    right -=1
                else:
                    while left<right and nums[left] == nums[left+1]:left+=1
                    left+=1
        return result

# write code here