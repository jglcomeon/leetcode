mylist = eval(input())
n = input()
x = int(input())

ans = 10 ** 9
new_x = x
for i in range(n):
    new_x = new_x - mylist[i]
    if new_x == 0:
        ans = i + 1
        break
    elif new_x < 0:
        break
new_x2 = x
for i in range(n-1, -1, -1):
    new_x2 = new_x2 - mylist[i]
    if new_x2 == 0:
        ans = min(ans, n -i)
        break
    elif new_x2 < 0:
        break
left_list = []
res = 0
for tem in mylist:
    res += tem
    left_list.append(res)
right_list = []
res = 0
for tem in mylist[::-1]:
    res += tem
    right_list.append(res)
right_list = right_list[::-1]

for i in range(n):
    for j in range(n-1,-1,-1):
        if left_list[i] + right_list[j] == x:
            ans = min(ans, i+1+n-j)
if ans == 10**9:
    print(-1)
else:
    print(ans)