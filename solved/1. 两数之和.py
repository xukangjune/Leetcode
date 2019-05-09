class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            if target - nums[i] in nums[:i]:
                return nums.index(target-nums[i]), i

a = [2,7,11,15]
t = 9
solve = Solution()
print(solve.twoSum(a, t))
