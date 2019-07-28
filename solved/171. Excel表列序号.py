"""
另见168题
"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        ret = 0
        for char in s:
            ret = ret * 26 + ord(char) - 64
        return ret

        # 想复杂了
        # i = 0
        # ret = 0
        # for char in s[::-1]:
        #     ret += (ord(char) - 64) * 26 ** i
        #     i += 1
        # return ret


solve = Solution()
print(solve.titleToNumber("CFDGSXM"))