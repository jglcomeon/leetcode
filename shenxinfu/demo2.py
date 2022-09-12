


T = int(input())
nums = []
for i in range(T):
    n = int(input())
    N = 2 + 1000000
    arr = [0] * N
    max_value = 0
    for j in range(n):
        s, e = map(int, input().split(' '))
        arr[s] += 1
        arr[e+1] -= 1
        c = 0
    for i in range(750000):
        c += arr[i]
        if c > max_value:
            max_value = c
    print(max_value)

