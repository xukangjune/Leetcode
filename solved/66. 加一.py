"""
本题为了给数组加一。从最后一位开始，最麻烦的该位等于9，加1就得进位。所以从后向前遍历。最后一位加一，如果大于十，则该位变成零，并向前接着遍历。
如果小于十，则直接返回数组。
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        for i in range(length-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits


solve = Solution()
digits = [1,2,9]
print(solve.plusOne(digits))