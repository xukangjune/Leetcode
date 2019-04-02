"""
先排序，然后选取最后三个数的乘积，以及最后一个数与前两个数的乘积，取最大者。无论正负数字的数目多少，这两个乘积里面一定有最大值
"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[0] * nums[1], nums[-1] * nums[-2] * nums[-3])



solve = Solution()
nums = [-4,-3,-2,-1,60]
print(solve.maximumProduct(nums))