class Solution:
    def wordCount(self, startWords, targetWords) -> int:
        newStart = []
        for i in startWords:
            newStart.append("".join(sorted(i)))

        res = 0

        for i in targetWords:
            for j in range(len(i)):
                temp = "".join(sorted(i[:j] + i[j+1:]))
                if temp in newStart:
                    res += 1
                    break
        return res

if __name__ == '__main__':
    s = Solution()
    s.wordCount(["ant","act","tack"],
                ["tack","act","acti"])

