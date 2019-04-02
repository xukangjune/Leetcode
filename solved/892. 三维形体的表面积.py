"""
这一题比较简单，只要单独考虑每一列和每一行。在遍历时可以将序号相同的列和行同时考虑，减少了运算量。但是最右侧和最
下面要单独考虑。
还有就是上下表面的问题，由于会遍历整个数组，所以只要判断当前遍历到的位置有没有立方体存在就好了。
"""
class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 1:
            return 6 + 4 * (grid[0][0] - 1)
        ret = 0
        for k in range(n):
            left, forward, j = 0, 0, 0
            while j < n:
                if grid[k][j]:             # 如果当前位置有立方体存在，那么加上上表面和下表面
                    ret += 2
                ret += abs(grid[k][j] - left)      # 当前位置的立方体与左边立方体的相交面
                ret += abs(grid[j][k] - forward)   # 当前位置的立方体与前面立方体的相交面
                left, forward, j = grid[k][j], grid[j][k], j + 1
            ret += grid[k][j-1]            # 加上每一行最右侧的面积
            ret += grid[j-1][k]            # 加上每一行最下面的面积
        return ret


solve = Solution()
# grid = [[2,2,2],[2,1,2],[2,2,2]]
# grid = [[1,1,1],[1,0,1],[1,1,1]]
# grid = [[1,2],[3,4]]
# grid = [[1,0],[0,2]]
grid = [[2]]
print(solve.surfaceArea(grid))