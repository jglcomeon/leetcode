def demo2(n, p, q, nums):
    arr1 = [0] * 10000000
    arr2 = [0] * 10000000
    for l, r, t in nums:
        if t == 1:
            for i in range(l, r + 1):
                arr1[i] += 1
        else:
            for i in range(l, r + 1):
                arr2[i] += 1
    res = 0
    for i in range(1, 10000000):
        if arr1[i] >= p and arr2[i] >= q:
            res += 1
    print(res)


if __name__ == '__main__':
    n, p, q = map(int, input().strip().split(' '))
    nums = []

    for i in range(3):
        nums.append(list(map(int, input().strip().split(' '))))
    nums = [[i[j] for i in nums] for j in range(len(nums[0]))]
    demo2(n, p, q, nums)