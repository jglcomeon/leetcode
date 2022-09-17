def demo1(s):
    res = ""

    def dfs(s, index):
        nonlocal res
        if index == len(s):
            return False
        if index == len(s) - 1:
            for i in range(10):
                if s[index-1] != str(i):
                    temp_s = s[:-1] + str(i)
                    if int(temp_s) % 3 == 0:
                        res = temp_s
                        return True
            return False
        if s[index] != '?':
            dfs(s, index+1)
        else:
            for i in range(10):
                if i == 0 and index == 0:
                    continue
                if s[index-1] != str(i) and s[index+1] != str(i):
                    temp = s
                    s = s[:index] + str(i) + s[index+1:]
                    flag = dfs(s, index+1)
                    if flag:
                        return True
                    else:
                        s = temp
        return True
    dfs(s, 0)
    print(res)

    

if __name__ == '__main__':
    s = input().strip()
    demo1(s)
    
    # ?12?0?9??