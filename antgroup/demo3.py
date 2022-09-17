from  collections import Counter

s = input().strip()

n = len(s)

a = [""]
for c in s:
    a.extend([x+c for x in a])
res = 0
r = []
for i in a:

    if not i:
        continue
    if len(i) % 2 != 0:
        continue
    tt = Counter(i)
    flag =True
    for j in tt:
        if tt[j] % 2 == 0:
            continue
        else:
            flag = False
            break
    if flag:

        # r.append(i)
        res += 1

print(res)
# print(a)
# print(r)