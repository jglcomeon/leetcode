def demo2(n, nums):
    dp = [0 for i in range(n)]
    dp[0] = len(nums)
    for i in range(1, n):

        left = 0
        right = i

        while right < n:
            if nums[right] - nums[right-1] == 1:
                t = right - left
                if t == i:
                    dp[i] += 1

            else:
                left = right
            right += 1
    new_arr = []
    for i in dp:
        new_arr.append(str(i))
    print(" ".join(new_arr))


if __name__ == '__main__':
    n = int(input().strip())
    nums = list(map(int, input().strip().split(' ')))
    if n == 1:
        print(1)
    else:
        demo2(n, nums)