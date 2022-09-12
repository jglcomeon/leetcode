'''
@Project ：leetcode 
@File    ：al_test0.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/7 7:41 下午 
'''

def test1(num):
    res= []
    # 遍历2~16进制的所有可能
    for i in range(2, 17):
        try:
            res.append(str(int(num, base=i)))
        except Exception as e:
            continue
    print("\n".join(res))


if __name__ == '__main__':
    num = input().strip()
    test1(num)



