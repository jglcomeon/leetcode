line = [i.strip("(") for i in input().strip().split(")")[:-1]]

line = [int(i[2:]) if i[1] == "+" else (-1*int(i[2:])) for i in line]
one_shot = 1
zero_shot = line[0]

for i in line[1:]:
    temp = 0
    temp += one_shot*i
    temp += zero_shot
    one_shot = temp
    zero_shot = zero_shot * i

print(one_shot % 10007)