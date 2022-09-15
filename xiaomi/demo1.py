import numpy as np
def demo2(m, a, n, b):

    # a1 = np.array(a)
    # b1 = np.array(b)
    res = np.convolve(a,b,mode='full').tolist()
    res.insert(0, len(res))
    if m < n:
        a = a + [0] * (n-m)
    elif n < m:
        b = b + [0] * (m-n)
    res2 = np.correlate(a,b,mode='full').tolist()
    res2.insert(0, len(res2))
    for index, i in enumerate(res):
        if i < 0:
            i = i % -2147483648
        else:
            i = i % 2147483647
        if index == 0:
            print(i, end=',')
        else:

            print(i, end=' ')
    print('\n')
    for index, i in enumerate(res2):
        if i < 0:
            i = i % -2147483648
        else:
            i = i % 2147483647
        if index == 0:
            print(i, end=',')
        else:

            print(i, end=' ')




if __name__ == '__main__':
    m, a = input().strip().split(',')
    m = int(m)
    a = list(map(int, a.strip().split(' ')))

    n, b = input().strip().split(',')
    n = int(n)
    b = list(map(int, b.strip().split(' ')))
    demo2(m, a, n, b)
