class Solution:
    def getMaximumGold(self, grid) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        ret = 0

        def dfs(i, j, cnt):
            nonlocal ret
            ret = max(ret, cnt)
            tmp = grid[i][j]
            grid[i][j] = 0
            for dir in dirs:
                x = i+dir[0]
                y = j+dir[1]
                if 0<=x<m and 0<=y<n and grid[x][y] != 0:
                    dfs(x, y, cnt+grid[x][y])
            grid[i][j] = tmp

        available = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    available.append([i, j])

        for pos in available:
            ret = max(ret, grid[pos[0]][pos[1]])
            dfs(pos[0], pos[1], grid[pos[0]][pos[1]])

        return ret


solve = Solution()
# grid = [[0,6,0],[5,8,7],[0,9,0]]
grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# grid = [[0,0,34,0,5,0,7,0,0,0],[0,0,0,0,21,0,0,0,0,0],[0,18,0,0,8,0,0,0,4,0],[0,0,0,0,0,0,0,0,0,0],[15,0,0,0,0,22,0,0,0,21],[0,0,0,0,0,0,0,0,0,0],[0,7,0,0,0,0,0,0,38,0]]
print(solve.getMaximumGold(grid))
