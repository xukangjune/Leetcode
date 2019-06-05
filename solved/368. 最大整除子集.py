"""
看解答都和我的雷同。时间复杂度为平方。首先建立一个列表来记录原列表每一位与前面的数字能够组成的最大的整除子序列，嗯，就这样
"""
class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        subsets = [[nums[i]] for i in range(n)]
        for i in range(n):
            tempSub = []
            tempLen = 0
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if len(subsets[j]) > tempLen:
                        tempLen = len(subsets[j])
                        tempSub = subsets[j]
            subsets[i] = tempSub + subsets[i]
        print(subsets)
        return max(subsets, key=lambda x:len(x))


solve = Solution()
nums = [4,8,10,240]
print(solve.largestDivisibleSubset(nums))