"""
本体是杨辉三角的改进。输出第k层，简单的方法就是利用已经计算好的杨辉三角，直接输出第K个元素。但是题目要求空间复杂度为O(n)。
所以直接生成一个数组，长度为k+1，然后在此数组上进行迭代操作。要记住，每一层都是对称的，因此求解一般就可以了。而且每一层的
遍历都应该从中间往两边走，如果反过来，就可能导致中间的数变大。
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1] * (rowIndex + 1)
        if rowIndex > 1:
            for i in range(2, rowIndex+1):
                print(i)
                for j in range(i//2, 0, -1):
                    ret[j] += ret[j-1]
                    ret[i-j] = ret[j]
        return ret


solve = Solution()
print(solve.getRow(5))
