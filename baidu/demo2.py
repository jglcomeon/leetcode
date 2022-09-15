import heapq


def demo2(n, m, nums, options):
    h = []
    for i, (t, k) in enumerate(options):
        heapq.heappush(h, (-k, t, i))
    now_index = -1
    for i in range(m):
        k, t, idx = heapq.heappop(h)
        k = k * (-1)
        if idx > now_index:
            new_arr = nums[:k]
            if t == 1:
                new_arr.sort()
            else:
                new_arr.sort(reverse=True)
            nums = new_arr + nums[k:]
            now_index = idx
        if idx == m - 1:
            break
    new_nums = []
    for i in nums:
        new_nums.append(str(i))
    print(" ".join(new_nums))


if __name__ == '__main__':

    n, m = map(int, input().strip().split(' '))

    nums = list(map(int, input().strip().split(' ')))
    options = []
    for i in range(m):
        t, k = map(int, input().strip().split(' '))
        options.append([t, k])

    demo2(n, m, nums, options)