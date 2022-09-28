def demo1(name, typed):
    m = len(name)
    n = len(typed)
    index1 = 0
    index2 = 0
    while index2 < n:
        if index1 < m and name[index1] == typed[index2]:
            index1 += 1
            index2 += 1
        elif index2 > 0 and typed[index2] == typed[index2-1]:
            index2 += 1
        else:
            print(0)
            return
    if index1 == m:
        print(1)


if __name__ == '__main__':
    name, typed = input().strip().split(' ')
    demo1(name, typed)
