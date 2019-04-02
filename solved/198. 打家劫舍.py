"""
动态规划，状态转移方程为dp[i] += max(dp[i-2], dp[i-3])，注意数组的大小进行操作。
还有可以直接在原数组上操作。
"""
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # 逆序
        # nums[n-3] += nums[n-1]
        # for i in range(n-4, -1, -1):
        #     nums[i] += max(nums[i+2], nums[i+3])
        # return max(nums[0], nums[1])

        # 顺序
        nums[2] += nums[0]
        for i in range(3, n):
            nums[i] += max(nums[i-2], nums[i-3])
        print(nums)
        return max(nums[n-1], nums[n-2])

solve = Solution()
nums = [1,2,3,1]
print(solve.rob(nums))