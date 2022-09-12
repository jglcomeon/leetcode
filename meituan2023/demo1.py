'''
@Project ：leetcode 
@File    ：demo1.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/8/6 10:05 上午 
'''

def demo1(x, y):
    res = 0
    t1 = min(x, y)
    t2 = x + y - t1
    temp = t2 // 2
    if temp >= t1:
        print(t1)
        return

    res += temp
    t2 = t2 - temp*2
    t1 -= temp
    if t1 >=2 and t2 == 1:
        res += 1

    print(res)


def demo12(x, y):
    print(min((x+y)//3, x ,y))


if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        x, y = map(int, input().split(' '))
        demo1(x, y)
        demo12(x,y)
