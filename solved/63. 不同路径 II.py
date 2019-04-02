"""
这一题和前面的题目类似，我还是在原始数组上操作，但这一点和之前的题目有点不同。首先，在最后一行和最后一列如果某个位置出现障碍物，由于这些位置
的离线是唯一的，所以如果出现障碍物，路线就被堵死了，之前的要通过这些位置的全部都要设为0。第二点，在数组内部遍历的过程中，假如遇见障碍物就直接
设为0，其它的就按正常情况来处理，即当前的位置路线等于下方位置的路线加上左方位置的路线。
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:   # 最特殊的情况，终点或起点被阻挡，那么总路线等于零
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m-1, -1, -1):  # 检查最后一列，如果出现1，则该位置上面的所有的位置都设为零
            if obstacleGrid[i][n-1] == 0:
                obstacleGrid[i][n-1] = 1
            else:
                for i1 in range(i, -1, -1):
                    obstacleGrid[i1][n-1] = 0
                break
        print(obstacleGrid)
        for j in range(n-2, -1, -1):  # 检查最后一行，如果出现1，则该位置前面的所有的位置都是无法通过的，所以路线为1
            if obstacleGrid[m-1][j] == 0:
                obstacleGrid[m-1][j] = 1
            else:
                for j1 in range(j, -1, -1):
                    obstacleGrid[m-1][j1] = 0
                break
        print(obstacleGrid)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] == 1 else obstacleGrid[i+1][j] + obstacleGrid[i][j+1]
        print(obstacleGrid)
        return obstacleGrid[0][0]


solve = Solution()
# a = [
#   [0,0,0],
#   [0,1,1],
#   [0,0,0]
# ]
# a = [[0]]
# a = [[1, 0]]
a = [[0,0],[1,0]]
print(solve.uniquePathsWithObstacles(a))