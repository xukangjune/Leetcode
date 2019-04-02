"""
比较简单，直接遍历一遍。如果是一就计数，如果是零，就进行比较count与ret。注意，最后还要将count与ret比较，
因为如果最后连续为1，那么在遍历结束后，不出现count与ret的比较。
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0 and count != 0:
                ret = count if count > ret else ret
                count = 0
        return count if count > ret else ret


solve = Solution()
nums = []
print(solve.findMaxConsecutiveOnes(nums))