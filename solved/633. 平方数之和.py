"""
本不想用sqrt函数，但是最后还是用了，并加以双指针。
但是最快的解法我看不懂，应该是和数学有关。
"""
from math import sqrt
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        j = int(sqrt(c))
        i = 0
        while i <= j:
            temp = i ** 2 + j ** 2
            if temp > c:
                j -= 1
            elif temp < c:
                i += 1
            else:
                return True
        return False


solve = Solution()
print(solve.judgeSquareSum(10))
