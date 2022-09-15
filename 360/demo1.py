
def demo1(nums, options):
    n = len(nums)
    for t, x in options:
        if t == 1:
            if x == 1:
                continue
            if x == n:
                nums.sort()
                continue
            temp = sorted(nums[:x])
            nums = temp + nums[x:]
        else:
            if x == 1:
                continue
            if x == n:
                nums.sort(reverse=True)
                continue
            temp = sorted(nums[:x], reverse=True)
            nums = temp + nums[x:]
    new_nums = []
    for i in range(len(nums)):
        new_nums.append(str(nums[i]))
    print(" ".join(new_nums))


if __name__ == '__main__':
    N, M = map(int, input().strip().split(' '))
    nums = list(map(int, input().strip().split(' ')))
    options = []
    for i in range(M):
        t, x = map(int, input().strip().split(' '))
        options.append((t, x))
    demo1(nums, options)