"""
本题要使用是回溯算法，用到了递归算法。先遍历数组，从中挑选一个数，然后将其余的数组加入递归函数中。递归函数返回的是传入数组
所能组成的所有的全序列组合。返回到上层函数后，只要将当前遍历到的数加上返回数组中所有的数组，组成一个新的数组。完全遍历结束
后，返回所有的数组组成的总数组
"""
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 1:
            return [nums]
        ret = []
        for i in range(len(nums)):
            temp = self.permute(nums[:i]+nums[i+1:n])
            ret += [[nums[i]]+num for num in temp]
        return ret


solve = Solution()
nums = [1,2,3]
print(solve.permute(nums))