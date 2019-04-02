"""
我用的方法比较简单，由于三阶幻方矩阵个数有限，所以先存在集合中，由于数组不能hash，所以先转为元组。然后使用列表解析，在所给的数组中选取三阶
的矩阵（转为元组），然后看是否在集合中。
"""
class Solution:
    # 直接先将所有的幻方矩阵存储下来，由于个数有限且比较少，能够存储
    squires = set()
    squires.add(((8, 1, 6), (3, 5, 7), (4, 9, 2)))
    squires.add(((6, 1, 8), (7, 5, 3), (2, 9, 4)))
    squires.add(((4, 9, 2), (3, 5, 7), (8, 1, 6)))
    squires.add(((2, 9, 4), (7, 5, 3), (6, 1, 8)))
    squires.add(((6, 7, 2), (1, 5, 9), (8, 3, 4)))
    squires.add(((8, 3, 4), (1, 5, 9), (6, 7, 2)))
    squires.add(((2, 7, 6), (9, 5, 1), (4, 3, 8)))
    squires.add(((4, 3, 8), (9, 5, 1), (2, 7, 6)))

    def numMagicSquaresInside(self, grid):

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 这个解法好像有点蠢，比较快，但是没有比较局限（只适合三阶的幻方矩阵）
        n = len(grid)
        k = len(grid[0])
        ret = 0
        for i in range(n-2):
            for j in range(k-2):
                # 使用列表解析
                new = tuple(tuple(grid[a][b] for b in range(j, j+3)) for a in range(i, i+3))
                # new = ((grid[i][j], grid[i][j+1], grid[i][j+2]), (grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]),
                #        (grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]))
                if new in self.squires:
                    ret += 1
        return ret





solve = Solution()
grid =  [[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]]
print(solve.numMagicSquaresInside(grid))