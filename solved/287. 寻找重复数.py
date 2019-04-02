"""
与142题环形链表Ⅱ一个套路。由于数字的大小不会超过下标，所以用数值作为下标可以建立一个循环链表。然后按照142题的套路就可以
完成。
"""
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


solve = Solution()
# nums = [1,3,2,2,2]
nums = [3,1,3,4,2]
# nums = [2,2,2,2,2]
# nums = [1,4,4,2,4]
# nums = [2,5,9,6,9,3,8,9,7,1]
print(solve.findDuplicate(nums))