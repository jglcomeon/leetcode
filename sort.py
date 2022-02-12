
def fast_sort(left, right, nums):
    l = left
    r = right
    temp = nums[left]
    while l < r:
        while nums[r] > temp and r > l:
            r -= 1
        if r > l:
            nums[l] = nums[r]
            l += 1
        while nums[l] < temp and r >l:
            l += 1
        if r > l:
            nums[r] = nums[l]
            r -= 1
    nums[l] = temp
    if l-1 > left:
        fast_sort(left, l-1, nums)
    if right > l+1:
        fast_sort(l+1, right, nums)


if __name__ == '__main__':
    nums = [5,4,1,7,9,-10]
    fast_sort(0, 5, nums)
    print(nums)