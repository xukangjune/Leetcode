"""
本题可以使用DP来解题，但是看解答只要数组的长度是偶数，就说明先手的人一定会赢。所以本题直接返回True。
这么理解，假设数组的长度位n（偶数），那么数组元素下标范围为0<=index<=n-1，即下标有一半为偶数，另一半为奇数。题目中说，所有堆的总石头数是奇
数，所以所有下标为偶数的所有的元素和要么大于奇数下标的元素和，要么小于。而先手的人能够完全确定自己一定能够自己拿到下标为奇数或偶数的元素。这
样可以事先先观察下标为偶数还是奇数时总数最大，然后自己去选择。
"""
class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[piles[i] if i == j else 0 for i in range(n)] for j in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][n-1] > 0


solve = Solution()
piles = [5,3,4,5]
print(solve.stoneGame(piles))