"""
这个和之前做的题很像，都是寻找二维数组中下降最快的路径，我是直接在原数组上操作，没有使用额外的空间。从下向上，每一层中每个数都要相加下面一层
三个数中最小的（首尾单独考虑），到最上面一层后，返回最小的一个值就好了。
"""
class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # 直接在原数组上操作,没有使用额外的空间。
        n = len(A)
        for i in range(n-2, -1, -1):  # 从下到上
            for j in range(1, n-1):
                A[i][j] += min(A[i+1][j-1], A[i+1][j], A[i+1][j+1])
            A[i][0] += min(A[i+1][0], A[i+1][1])
            A[i][n-1] += min(A[i+1][n-1], A[i+1][n-2])
        return min(A[0])


solve = Solution()
# A = [[0]]
A = [[1,2],[3,4]]
# A = [[1,2,3],[4,5,6],[7,8,9]]
print(solve.minFallingPathSum(A))