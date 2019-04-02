"""
比较简单，但这类题目有一点要注意，就是最后的temp要与ret比较大小，因为假如最后的数组一直递增的话，就不会出现if语句中的比较。
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp += 1
            else:
                ret = temp if temp > ret else ret
                temp = 1
        return ret if not nums else max(ret, temp)



solve = Solution()
nums = [1,3,5,2,7]
print(solve.findLengthOfLCIS(nums))