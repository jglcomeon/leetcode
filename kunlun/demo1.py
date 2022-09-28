#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param arr int整型一维数组
# @return int整型
#
class Solution:
    def max_wave_arr_len(self, arr) -> int:
        # write code here
        res = 0
        n = len(arr)
        left = 0
        record = []
        for i in range(1, n):
            if arr[i] - arr[i - 1] > 0:
                record.append(1)
            else:
                record.append(0)
        left = 0
        if n == 1:
            return 1
        while left < n - 1:
            t = left + 1

            while t < n-1 and record[t] ^ record[t - 1]:
                t += 1
            res = max(res, t - left)
            left = t
        print(res)



if __name__ == '__main__':
    s = Solution()
    s.max_wave_arr_len([1,2,1,2,1])