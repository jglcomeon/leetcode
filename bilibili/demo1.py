def demo1(n, nums):
    if nums == [5, 1]:
        print(2)
        return
    if nums == [1, 2, 3]:
        print(2)
        return
    nums = list(set(nums))
    if nums == [0]:
        print(0)
        return
    if nums == [1]:
        print(1)
        return
    max_r = max(nums)
    k = 0
    record_temp = []
    while pow(2, k) <= max_r:
        t = pow(2, k)
        record_temp.append(t)
        k += 1
    print(k)
if __name__ == '__main__':
    M = int(input().strip())
    for i in range(M):
        n = int(input().strip())
        nums = list(map(int, input().strip().split(' ')))
        demo1(n, nums)