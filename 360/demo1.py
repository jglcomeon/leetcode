
def demo1(nums, options):
    n = len(nums)
    for t, x in options:
        if t == 0:
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
    N, M = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    options = []
    for i in range(M):
        t, x = map(int, input().split(' '))
        options.append((t, x))
    demo1(nums, options)