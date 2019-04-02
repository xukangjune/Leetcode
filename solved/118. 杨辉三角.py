"""
本题是求解杨辉三角，可以根据上一层的值求解下一层，有点像DP
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [[1] * i for i in range(1, numRows+1)]
        for i in range(1, numRows):
            for j in range(1, i):
                ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
        return ret


solve = Solution()
print(solve.generate(5))