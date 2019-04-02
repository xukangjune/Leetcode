class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        num = x
        newNum = 0
        while num != 0:
            newNum = newNum * 10 + num % 10
            num //= 10
        return x == newNum


solve = Solution()
print(solve.isPalindrome(0))