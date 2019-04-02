"""
数组最大子序列乘积，先顺序遍历，返回值ret先初始为第一个元素，然后temp=1，然后拿遍历的数与temp相乘，如果大于ret，那么ret重新赋值，就这样在
没有遇到零之前，一直乘下去，因为负负得正，所以遇到负数也不要停下来。
但是这样会遇到一个问题，假设有一列负数的顺序为 -3 -4 -5，那么很显然选择-4和-5，但是顺序遍历是不会得到这样的结果的，所以我的方法是接着逆序
遍历一遍，这样就能得到最后的结果。
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        temp = 1
        for i in nums:
            temp *= i
            ret = temp if temp > ret else ret
            temp = 1 if temp == 0 else temp
        temp = 1
        for i in nums[::-1]:
            temp *= i
            ret = temp if temp > ret else ret
            temp = 1 if temp == 0 else temp
        print(ret)
        return ret

solve = Solution()
a = [0, 0, 1]
solve.maxProduct(a)