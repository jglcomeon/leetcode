'''
@Project ：leetcode 
@File    ：test2.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/6 11:17 上午 
'''
def test2(s):
    transformers = {'A':10,'a':10, 'B':11, 'b':11, 'C':12, 'c':12, 'D':13,
                    'd':13, 'E':14,'e':14, 'F':15, 'f':15}
    res = 0
    cnt = 0
    for i in reversed(s):

        if '0' < i < '9':
            res += int(i) * (16**cnt)
        elif transformers.get(i, '')!='':
            res += transformers[i] * (16**cnt)
        else:
            print(res)
            return
        cnt += 1



if __name__ == '__main__':
    s = input().strip()
    test2(s)

