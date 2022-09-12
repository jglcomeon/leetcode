'''
@Project ：leetcode 
@File    ：test1.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/6 11:08 上午 
'''

def test1(num):
    return num // 2

if __name__ == '__main__':
    while 1:
        temp = int(input())
        if temp == 0:
            break
        print(test1(temp))

