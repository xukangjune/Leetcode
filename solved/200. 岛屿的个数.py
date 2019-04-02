"""
这一题没有用并差集呀！
用的深搜，很直观，先便利二维数组，遇到1后，先ret加1，接着从此位置开始找出所有的“相连”的1，并设为0，后续遍历的
时候就不会遇到这些1了，能遇到的1说明就是新的岛。
又用了广搜，也比较简单，不用递归直接迭代。
看了用并查集的解法，很复杂（https://leetcode.com/problems/number-of-islands/discuss/56354/1D-Union-Find-Java-solution-easily-generalized-to-other-problems）
由于是二维数组，这里建立了一个一维数组来代替二位数组的所有点，其中grid[i][j]在一维数组中的位置就是i*row+j，初始值
也为这么多。然后就是在原数组中找到两个相连的1，进行并查集的操作，找寻各自根节点，然后判断根节点是否相同，不同就设置为
同一根节点。
先统计所有1的个数（即初始所有岛的个数），然后每合并两个岛就从总个数中减去1。
"""
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 没有用并查集， 直接用的深度优先搜索
        ret = 0
        if grid:
            col = len(grid)
            row = len(grid[0])

            # 深搜
            # def dfs(i ,j):
            #     grid[i][j] = "0"
            #     if i > 0 and grid[i-1][j] == "1":
            #         dfs(i-1, j)
            #     if i < col-1 and grid[i + 1][j] == "1":
            #         dfs(i+1, j)
            #     if j > 0 and grid[i][j - 1] == "1":
            #         dfs(i, j-1)
            #     if j < row-1 and grid[i][j + 1] == "1":
            #         dfs(i, j+1)

            # 广搜
        #     def bfs(pos):
        #         while pos:
        #             print(pos)
        #             temp = []
        #             for point in pos:
        #                 i, j = point[0], point[1]
        #                 grid[i][j] = "0"
        #                 if i > 0 and grid[i - 1][j] == "1":
        #                     temp.append([i - 1, j])
        #                 if i < col - 1 and grid[i + 1][j] == "1":
        #                     temp.append([i + 1, j])
        #                 if j > 0 and grid[i][j - 1] == "1":
        #                     temp.append([i, j - 1])
        #                 if j < row - 1 and grid[i][j + 1] == "1":
        #                     temp.append([i, j + 1])
        #             pos = temp
        #
        #     for i in range(col):
        #         for j in range(row):
        #             if grid[i][j] == "1":
        #                 ret += 1
        #                 # dfs(i, j)
        #                 bfs([[i, j]])
        # return ret




solve = Solution()
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
# grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(solve.numIslands(grid))