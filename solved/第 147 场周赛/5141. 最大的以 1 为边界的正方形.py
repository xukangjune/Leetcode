class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        ret = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                pass