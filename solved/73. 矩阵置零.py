"""
用python写简单一点。首先由于是动态类型语言，所以列表内元素的类型不一定要一致，所以在dfs的过程中将要换成0的位置，全部换成‘#’。然后遇到0的时候，递归。
这样最后时，将所有是‘#’的地方全部换成0即可。
"""
class Solution:
    def setZeroes(self, matrix) -> None:
        m = len(matrix)
        n = len(matrix[0])
        def dfs(x, y):
            for i in range(m):
                if i != x and not matrix[i][y]:
                    dfs(i, y)
                else:
                    matrix[i][y] = '#'
            for j in range(n):
                if j != y and not matrix[x][j]:
                    dfs(x, j)
                else:
                    matrix[x][j] = '#'

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    dfs(i, j)


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0


solve = Solution()
# a = [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# a = [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
a = [[0,1]]
solve.setZeroes(a)
print(a)