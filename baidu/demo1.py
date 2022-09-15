def demo1(n, m, t, nums1, nums2):
    s1 = []
    s2 = []
    total = 0

    for i in range(n):
        total += nums1[i]
        if total > t:
            break
        s1.append(total)
    total = 0
    for i in range(m):
        total += nums2[i]
        if total > t:
            break
        s2.append(total)
    res = 0
    for i in reversed(range(len(s1))):
        for j in reversed(range(len(s2))):
            if s1[i] + s2[j] <= t:
                res = max(res, i+j+2)
    print(res)


if __name__ == '__main__':
    n, m, t = map(int, input().strip().split(' '))
    nums1 = list(map(int, input().strip().split(' ')))
    nums2 = list(map(int, input().strip().split(' ')))
    demo1(n, m, t, nums1, nums2)