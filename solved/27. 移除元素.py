"""
题目的意思是将数组中的val移到最后，而不是直接删除。所以用两个指针，一个指向第一个元素，另一个指向最后一个。当尾指针等于val时，尾指针减一，
当头指针等于val时，头尾指针交换，且尾指针减一。只要涉及头指针，最后头指针就要加一。
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        while first < last:
            if nums[last] == val:
                last -= 1
                continue
            if nums[first] == val:
                nums[first], nums[last] = nums[last], nums[first]
                last -= 1
            first += 1
        return first if last < 0 or nums[first] == val else first + 1


solve = Solution()
nums = []
val = 0
print(solve.removeElement(nums, val))
print(nums)