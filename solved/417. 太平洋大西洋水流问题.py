"""
有点慢，但是我看其他人做的也是用深搜和广搜做的，所欲i思路都一样。原来做的时候想的比较复杂，其实这就是两个问题的综合。先求出到太平洋的山峰，然后求出
到大西洋的山峰，最后找共同的山峰就可以了。
"""
class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        flags = [['@' for j in range(n)] for i in range(m)]

        def isLegal(i, j, height, sign):
            if 0 <= i < m and 0<= j < n and matrix[i][j] >= height and flags[i][j] != sign:
                return True
            return False

        def dfs(i, j, sign):
            ret = [[i, j]]
            for direction in directions:
                nextI = i + direction[0]
                nextJ = j + direction[1]
                if isLegal(nextI, nextJ, matrix[i][j], sign):
                    flags[i][j] = sign
                    ret += dfs(nextI, nextJ, sign)
            return ret

        startsOfPacific = []
        ret1 = []
        for i in range(m):
            flags[i][0] = '#'
            startsOfPacific.append([i, 0])
        for j in range(n):
            flags[0][j] = '#'
            startsOfPacific.append([0, j])
        for start in startsOfPacific:
            ret1 += dfs(start[0], start[1], '#')

        startsOfAtlantic = []
        ret2 = []
        for i in range(m):
            flags[i][n-1]  = '$'
            startsOfAtlantic.append([i, n-1])
        for j in range(n):
            flags[m-1][j]  = '$'
            startsOfAtlantic.append([m-1, j])
        for start in startsOfAtlantic:
            ret2 += dfs(start[0], start[1], '$')

        return [list(pos) for pos in set(map(tuple, ret1)) & set(map(tuple, ret2))]



solve = Solution()
#
m = [[1,2]]
print(solve.pacificAtlantic(m))