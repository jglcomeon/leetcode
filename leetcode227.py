'''
@Project ：leetcode 
@File    ：leetcode227.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/13 11:08 上午 
'''


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = ('+' + s).replace(" ", "")

        n = len(s)
        print(n)
        i = 1
        while i < n:
            if '0' <= s[i] <= '9':
                temp = s[i]
                time_t = i
                while i + 1 < n and '0' <= s[i+1] <= '9':
                    temp += s[i+1]
                    i += 1
                temp = int(temp)
                if s[time_t-1] == '+':
                    stack.append(temp)
                elif s[time_t-1] == '-':
                    stack.append(-temp)
                elif s[time_t-1] == '/':
                    t = stack.pop()
                    stack.append(int(t / temp))
                elif s[time_t-1] == '*':
                    t = stack.pop()
                    stack.append(t * temp)
            i += 1

        return sum(stack)

    def calculate2(self, s: str) -> int:
        stack1 = []
        stack2 = []
        dict = {'+': 1, '-': 1, '*': 2, '/': 2}
        n = len(s)
        i = 0
        res = 0
        while i < n:
            if '0' <= s[i] <= '9':
                temp = s[i]
                time_t = i
                while i + 1 < n and '0' <= s[i+1] <= '9':
                    temp += s[i+1]
                    i += 1
                temp = int(temp)
                stack1.append(temp)

            if dict.get(s[i], 0) != 0:
                if not stack2:
                    stack2.append(s[i])
                elif stack2 and dict[s[i]] >= dict[stack2[-1]]:
                    stack2.append(s[i])
                elif stack2 and dict[s[i]] < dict[stack2[-1]]:
                    t2 = stack1.pop()
                    t1 = stack1.pop()
                    t3 = stack2.pop()
                    if t3 == '+':
                        stack1.append(int(t1) + int(t2))
                    elif t3 == '-':
                        stack1.append(int(t1) - int(t2))
                    elif t3 == '/':
                        stack1.append(int(int(t1) / int(t2)))
                    else:
                        stack1.append(int(t1) * int(t2))
                    stack2.append(s[i])
            i += 1
            if i == n:
                if len(stack1) == 1:
                    return stack1[0]
                while stack1 and stack2:
                    t2 = stack1.pop()
                    t1 = stack1.pop()
                    t3 = stack2.pop()
                    if t3 == '+':
                        stack1.append(int(t1) + int(t2))
                    elif t3 == '-':
                        stack1.append(int(t1) - int(t2))
                    elif t3 == '/':
                        stack1.append(int(int(t1) / int(t2)))
                    else:
                        stack1.append(int(t1) * int(t2))
                    #stack2.append(s[i])
                print(stack1)
                return stack1[0]


if __name__ == '__main__':
    s = Solution()
    print(s.calculate2("1*2-3/4+5*6-7*8+9/10"))

