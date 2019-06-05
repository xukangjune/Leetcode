"""
我能想到就是平方级别的解法，后来看网上的解答为二分法，时间复杂度要小很多为nlogX，X为最大最小值之间的差值。其实就是线性级别的。因为第一数和最后一个数
分别时最大值和最小值，找出中间值后就可以在原数组中找出这个雄安与这个值的数目，这里找数目是有技巧的，充分利用了原数组在两个方向的递增的特点。最后一步步
缩小范围，直到lo==hi。在缩小的过程中，要注意lo和hi分别对mid的取值，这是因为count与k关系决定的。
"""
class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[n-1][n-1]
        while lo < hi:
            mid = (lo + hi) // 2
            j = n - 1
            count = 0
            for i in range(n):
                if j == -1:
                    break
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j+1)
            if count < k:
                lo = mid + 1
            else:
                hi = mid
        return lo


solve = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
print(solve.kthSmallest(matrix, 8))