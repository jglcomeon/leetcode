
def demo2(s):
    t1, t2 = s.split('=')
    raise Exception(s)
    if eval(t1) == eval(t2):
        return "Yes"
    t1_value = eval(t1)
    t2_value = eval(t2)
    if t1_value > t2_value:
        pass


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        s = input()
        temp_res = demo2(s)
        print(temp_res)
