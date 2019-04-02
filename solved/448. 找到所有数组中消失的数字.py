"""
题目要求不用额外空间，所以使用计数排序
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            cur = num-1 if num > 0 else -num-1
            if nums[cur] < 0:
                continue
            else:
                nums[cur] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]


solve = Solution()
nums = [4,3,2,7,8,2,3,1]
print(solve.findDisappearedNumbers(nums))