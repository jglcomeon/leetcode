from math import ceil


def test1(n, nums):
    if len(nums) == 1:
        print(n)
        return
    all_sum = n
    for i in range(len(nums)):
        all_sum = all_sum / (1 - nums[i]) - 0.000001
        all_sum = int(all_sum)

    print(int(all_sum))
if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    temp = input().split(' ')
    nums = []
    for i in temp:
        nums.append(float(i))
    test1(n, nums)