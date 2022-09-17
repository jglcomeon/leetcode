from collections import defaultdict


def demo33(s):
    dicts = defaultdict(int)
    res = 0
    cur = 0
    dicts[0] = 1
    for c in s:
        cur ^= (1 << (ord(c)-ord('a')))
        for i in range(26):
            res += dicts.get(cur ^ (1 << i), 0)
        dicts[cur] += 1
    print(res)


if __name__ == '__main__':
    s = 'ababa'
    demo33(s)