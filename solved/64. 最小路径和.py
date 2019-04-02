"""
和做过的很多题目类似，可以直接在原数组上操作，而不用开辟新空间。首先最后一列和最后一行的位置只有一种移动方式，所以这些位置的路径和就是直接加
上唯一方向的路径和。其余的位置就要将当前位置与右边和下边一个较小的值相加，得到的值就是当前位置的路径和。以此类推，最后得到的第一个位置的值就
是最小的路径和。
"""
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m-2, -1, -1):
            grid[i][n-1] += grid[i+1][n-1]
        for j in range(n-2, -1, -1):
            grid[m-1][j] += grid[m-1][j+1]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        print(grid)
        return grid[0][0]


solve = Solution()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(solve.minPathSum(grid))