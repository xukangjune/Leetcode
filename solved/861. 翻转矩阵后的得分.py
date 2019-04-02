"""
由于数组中的数作为二进制，所以第一位的数要大于其它所有位加起来的总和。所以第一将数组A中的每一项的第一位先反转成1.接下来，从第二列开始，分析
所有的列。由于每一列的每个数在二进制数中的位置相同，所以不管怎么变，要确保这一列中1的次数最多。可不敢按行反转，因为这样会破坏第一位的1。
首先，我也想到了zip函数，但是没有记起反组合。所以速度比较慢。
"""
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row = len(A)
        col = len(A[0])
        for i in range(row):
            if A[i][0] == 0:
                for j in range(col):
                    A[i][j] ^= 1
        # 网上解法
        newList = list(zip(*A))
        ret = row * 2 ** (col-1)
        for i in range(1,col):
            num_0 = newList[i].count(0)
            num_1 = row - num_0
            ret += max(num_0, num_1) * 2 ** (col-1-i)

        # 我的解法
        # for i in range(1, col):
        #     if sum([A[j][i] for j in range(row)]) < row / 2:
        #         for j in range(row):
        #             A[j][i] ^= 1
        # ret = 0
        # for bit in A:
        #     ret += int(''.join(str(i) for i in bit), 2)
        return ret


solve = Solution()
# A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# A = [[1,0,0,1]]
A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(solve.matrixScore(A))
print(A)