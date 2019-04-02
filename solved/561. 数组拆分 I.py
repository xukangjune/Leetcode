"""
也很简单呀
"""
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([nums[i] for i in range(0, len(nums), 2)])


solve = Solution()
nums = [-4,-3,-2,-7,-5,-10]
print(solve.arrayPairSum(nums))