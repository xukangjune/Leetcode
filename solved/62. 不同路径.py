"""
没什么特别的地方，使用动态规划，申请一个与原来的数组相等大小的数组，由于棋子只能向下或向右移动，所以最后一列和最后一行的值都设为1，其它先设为
0（其实用不着这样，可以先全部设为1，反正除了最后一行和最后一列所有的值在递归的过程中都需要重新赋值）。接下来开始从后先前遍历，每一个位置的路
线都是右边的位置的路线加上下面的路线。这样一直遍历下去，在dp[0][0]就是最后的总路线。
在网上看到另一种解法，使用排列组合的思想解决。因为机器人从起点到终点，一共要走m+n-2步，其中m-1步向右，n-1步向下。所以问题就变成了从m+n-2
个位置中选取m-1个位置，共有几种选法。所以可以直接使用阶乘来搞定。
"""
from math import factorial
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 中规中矩，动态规划
        # dp = [[1 if i == m-1 or j == n-1 else 0 for i in range(m)] for j in range(n)]
        # print(dp)
        # for i in range(m-2, -1, -1):
        #     for j in range(n-2, -1, -1):
        #         print(i, j)
        #         dp[j][i] = dp[j+1][i] + dp[j][i+1]
        # print(dp)
        # return dp[0][0]

        # 注意，前方高能。使用排列组合。
        return int(factorial(m + n - 2) / factorial(m -1) / factorial(n-1))


solve = Solution()
print(solve.uniquePaths(3, 3))