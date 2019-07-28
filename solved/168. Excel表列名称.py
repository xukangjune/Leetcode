"""
https://leetcode-cn.com/problems/excel-sheet-column-title/solution/jin-zhi-wen-ti-by-xukangjune-bcghruts2o/
"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = ""
        while n:
            print(n, n%26)
            k = n % 26
            if k == 0:
                ret = 'Z' + ret
                n -= 26
            else:
                ret = chr(k+64) + ret
            n //= 26
        return ret

solve = Solution()
print(solve.convertToTitle(78))