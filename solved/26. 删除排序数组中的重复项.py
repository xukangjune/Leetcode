"""
本题在前面设置一个pos，该位置前面的数据只出现一次，如果后面有新的数据加入，就可以直接将该位置赋值为新数据，然后将该位置向后移动一位。
等到遍历结束后，就可以直接输出pos了。
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp = nums[0]
        pos = 1
        for i in range(1, len(nums)):
            if nums[i] == temp:
                continue
            elif nums[i] > temp:
                temp = nums[i]
                nums[pos] = nums[i]
                pos += 1
        return pos


solve = Solution()
nums = [1]
print(solve.removeDuplicates(nums))