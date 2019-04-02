"""
很神奇，但是我不知道其中的数学原理。在给的数大于4的时候，只要将给的数分解成3与另一个数相乘即可。
"""
class Solution:
    dp = {}
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        def func(n):
            if n in self.dp:
                return self.dp[n]
            num = 3 * func(n-3)
            self.dp[n] = num
            return num
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        return func(n)



solve = Solution()
print(solve.integerBreak(11))