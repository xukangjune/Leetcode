"""
这一题我看了提示，其实就是将这个数组看成两段，一段从0~n-1, 一段从2~n，分别使用198题的方法，最后就可以得到结果。
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
        if n == 3:
            return max(nums[0], nums[1], nums[2])
        dp = [0] * n
        dp[0],dp[1] = nums[0], nums[1]
        dp[2] = nums[2] + nums[0]
        for i in range(3, n-1):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        ret = max(dp[n-2], dp[n-3])
        print("1=", dp)
        dp[2] = nums[2]
        dp[3] = nums[1] + nums[3]
        for i in range(4, n):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        print("2=", dp)
        return max(ret, dp[n-1], dp[n-2])


solve = Solution()
# nums = [2,3,2]
# nums = [1,2,3,1]
nums = [2,3,2,1,2,4,5,6,7,0,2,3,0,9,1,1,2,3]
print(solve.rob(nums))