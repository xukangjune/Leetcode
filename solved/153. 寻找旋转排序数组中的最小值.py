"""
简单，二分法，将中间数与右边数比较更好
"""
class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m
        return nums[l]