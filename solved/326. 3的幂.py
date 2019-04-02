"""
此题不用循环或者递归来做，在整数范围最大的3的n次幂为3^19==1162261467。所以所有3的幂都可以整除它，其它的数则不能。
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return 1162261467 % n == 0 if n > 0 else False

solve = Solution()
print(solve.isPowerOfThree(81))