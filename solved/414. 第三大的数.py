"""
这题本来想用计数排序的，但是对内存的要求太高。然后设置了三个变量，并为了消除重复元素的影响，先将数组转化为集合。然后遍历集合，依次与三个
数比较。
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        first = second = third = min(nums)
        for num in nums:
            if num > third:
                first, second, third = second, third, num
            elif num > second:
                first, second = second, num
            elif num > first:
                first = num
        return first if second > first else third


solve = Solution()
nums = [1, 2]
print(solve.thirdMax(nums))