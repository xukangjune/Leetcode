"""
这一题我是看网上的解法的。我的想法和该解法差不多，都是从外层逐步替换到内层。但是我的想法是一次性交换，这实现起来有点困难，现在的解法是逐个的交换。
规律如下：先设定两个变量i1，i2，i1先为0，i2为数组长度减1，首先外层遍历，要求i1小于i2，因为i1等于i2时，说明了要替换的数字为自己，说明替换过程
结束。内层的循环之前设定两个变量j1=i2,j2=i1，条件为j1不等于i1。然后四个位置一次交换。
核心是，每次交换完后，j2 += 1， j1 -= 1。这是因为再内部交换的过程中，i1，i2是不变的，位置的变化要用j2和j1来改变。j1等于i1的时候，说明内层的
循环已经处理好i2-1个位置了。
内层循环结束后，i1 += 1， i2 -= 1。说明外面一圈已经交换完，接下来该处理“内部”的位置了。
"""
class Solution:
    def rotate(self, matrix):
        if not matrix:
            return matrix
        i2 = len(matrix) - 1
        i1 = 0
        while (i1 < i2):
            j1 = i2
            j2 = i1
            while (j1 != i1):
                temp = matrix[i1][j2]
                matrix[i1][j2] = matrix[j1][i1]
                matrix[j1][i1] = matrix[i2][j1]
                matrix[i2][j1] = matrix[j2][i2]
                matrix[j2][i2] = temp
                j2 += 1
                j1 -= 1
            i1 += 1
            i2 -= 1

        print(matrix)


solve = Solution()
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
solve.rotate(matrix)