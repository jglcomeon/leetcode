#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：mergeSort.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/2/13 11:11 下午 
'''


class MergeSort:

    def sort(self, nums, l, r):
        if l < r:
            mid = (l + r) // 2
            self.sort(nums, l, mid)
            self.sort(nums, mid + 1, r)
            self.merge(nums, l, mid, r)

    def merge(self, nums, l, mid, r):
        temp = [0] * (r - l + 1)
        t_l = l
        t_r = mid + 1
        index = 0
        while t_l <= mid and t_r <= r:
            if nums[t_l] < nums[t_r]:
                temp[index] = nums[t_l]
                t_l += 1
            else:
                temp[index] = nums[t_r]
                t_r += 1
            index += 1
        if t_l <= mid:
            while t_l <= mid:
                temp[index] = nums[t_l]
                index += 1
                t_l += 1
        if t_r <= r:
            while t_r <= r:
                temp[index] = nums[t_r]
                index += 1
                t_r += 1
        nums[l:r+1] = temp


if __name__ == '__main__':
    s = MergeSort()
    nums = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]
    s.sort(nums, 0, len(nums)-1)
    print(nums)

