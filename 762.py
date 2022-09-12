'''
@Project ：leetcode 
@File    ：762.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/4/5 6:21 下午 
'''
import math


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        while left <= right:
            temp = left
            temp_count = 0
            while temp:

                temp_count += temp & 1
                temp = temp >> 1
            if self.prime_number(temp_count):
                count+=1
            left += 1
        return count

    def prime_number(self, num):
        n = int(math.sqrt(num))
        for i in range(2, n+1):
            if num % n == 0:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    s.countPrimeSetBits(6, 10)

