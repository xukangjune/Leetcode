"""
比较简单，和搜索二位矩阵Ⅰ相同。
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            col = 0
            row = n-1
            while col < m and row >= 0:
                if matrix[col][row] == target:
                    return True
                elif matrix[col][row] > target:
                    row -= 1
                else:
                    col += 1
        return False