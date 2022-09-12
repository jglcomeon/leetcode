'''
@Project ：leetcode 
@File    ：test1.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/28 7:18 下午 
'''

def test1(nums, n):
    if n == 1:
        print(str(nums[0]))
        return
    if n >= 2 and nums[1] != nums[0]:
        res = str(nums[0])

    else:
        res = ""
    count = 1
    for i in range(1, n):
        if nums[i] == nums[i-1]:
            count += 1
            if i == n-1:
                res += " " +str(nums[i-1]) + '(' + str(count) + ')'
                break

        else:
            if count != 1:
                res += " " +str(nums[i-1]) + '(' + str(count) + ')'
                count = 1
            if i < n-1 and nums[i] != nums[i+1]:
                res += " " + str(nums[i])
            if i == n - 1:
                res += " " + str(nums[i])
    print(res.strip())



if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split(' ')))
    test1(nums, n)