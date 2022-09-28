

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):

        m = int(input().strip())
        line = [int(i) for i in input().strip().split()]
        res = []
        l = len(line)
        for i in range(l):
            for j in range(i-1, -1, -1):
                if line[j] > line[i]:
                    res.append((str(line[j])))
                    break
            else:
                res.append("INF")
        print(" ".join(res))