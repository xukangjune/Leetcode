"""
本题要求在原数组上操作，所以先找出第一个零的位置，然后向后遍历，如果遇到数不是零，则与第一零交换位置，如果时零，则继续遍历。
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first = nums.index(0) if 0 in nums else None
        if first is None:
            return
        length = len(nums)
        for i in range(first+1, length):
            if nums[i] != 0:
                nums[first], nums[i] = nums[i], nums[first]
                first += 1


solve = Solution()
nums = [0,1,0,3,12]
solve.moveZeroes(nums)
print(nums)