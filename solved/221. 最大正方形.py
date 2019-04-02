"""
我只能想通这一个解法，动态规划，状态转移方程如下。
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxLength = 0
        # 内存消耗多，而且耗时也多
        # if matrix:
        #     m = len(matrix)
        #     n = len(matrix[0])
        #     maxLength = 0
        #     dp = [[0] * (n+1) for j in range(m+1)]
        #     for i in range(m-1, -1, -1):
        #         for j in range(n-1, -1, -1):
        #             if matrix[i][j] == '1':
        #                 dp[i][j] = 1 + min(dp[i+1][j], dp[i+1][j+1], dp[i][j+1])
        #                 maxLength  = maxLength if maxLength > dp[i][j] else dp[i][j]
        # return maxLength ** 2

        # 新的解法
        # if matrix:
        #     m = len(matrix)
        #     n = len(matrix[0])
        #     for i in range(m):
        #         for j in range(n):
        #             matrix[i][j] = int(matrix[i][j])
        #             if i == 0:
        #                 maxLength = 1 if not maxLength and matrix[i][j] == 1 else maxLength
        #             elif j == 0:
        #                 maxLength = 1 if not maxLength and matrix[i][0] == 1 else maxLength
        #             elif matrix[i][j]:
        #                 matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])
        #                 maxLength = maxLength if maxLength > matrix[i][j] else matrix[i][j]
        # return maxLength ** 2


        # 内存最小，有几种情况没有考虑
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i and j:
                    matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])
        return max(map(max, matrix)) ** 2



solve = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = []
print(solve.maximalSquare(matrix))