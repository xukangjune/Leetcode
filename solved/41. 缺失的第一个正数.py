"""
将元素的值与数组下标联系起来。首先如果元素的值在下标的范围内，则将其入位，下标的值要填入的时候进行修正，使其满足0.如果数组的值超过下标的范围，那么就不要操作。留在原地。
在改变数组后，最后遍历一遍数组，如果下标加一不等于数组中的数，那么说明这是第一个缺失的正数。如果遍历到最后都满足，那么说明下标加一也是满足的。
"""
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] < n and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp

        for i in range(n):
            if nums[i] != i + 1:
                print(i+1)
                return i + 1

solve = Solution()
a = [1, 1, 2]
solve.firstMissingPositive(a)
