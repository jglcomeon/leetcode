from collections import defaultdict, Counter



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(set(list(t)))
        if len(t) > n:
            return ""
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""

        left = 0
        right = 1
        dicts2 = Counter(t)
        res_left = 0
        res_right = n
        dicts = defaultdict(int)
        nums = set()
        if s[0] in t:
            dicts[s[0]] += 1
            if dicts[s[0]] >= dicts2[s[0]]:
                nums.add(s[0])
        flag = False
        while left < right and right < n:
            if s[right] in t:
                dicts[s[right]] += 1
                if dicts[s[right]] >= dicts2[s[right]]:
                    nums.add(s[right])

            while len(nums) == m:
                flag = True
                # if right - left + 1 == m:
                #     return s[left:right+1]
                t1 = right - left
                t2 = res_right - res_left
                if t1 < t2:
                    res_left = left
                    res_right = right
                if s[left] in t:
                    dicts[s[left]] -= 1
                    if dicts[s[left]] < dicts2[s[left]]:
                        nums.remove(s[left])
                left += 1

            right += 1

        if not flag:
            return ""
       
       
        return s[res_left:res_right+1]

if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("babb", "baba"))