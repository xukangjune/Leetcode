"""
移动一个长度为k的窗口，但是在累加时可以加上一个数并减去第一数，这样快一点。最后要注意的是，一定要将写成float（k）的形式。
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ret = sum(nums[:k])
        first = 0
        temp = ret
        for num in nums[k:]:
            temp += num - nums[first]
            ret = temp if temp > ret else ret
            first += 1
        return ret / float(k)


solve = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(solve.findMaxAverage(nums, k))