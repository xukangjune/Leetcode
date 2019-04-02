"""
本题有一个重要的数学知识，由于列表的元素只能赋予正号或负号，所以整个数组可以分为两部分，即正号和减负号和，即nums[positive]-nums[negative]
= S, 所以nums[positive]-nums[negative] + nums[positive] + nums[negative] = 2 X nums[positive] = S + sums[nums]。所以问题就
转化成了在nums中找出子集和等于temp = （S + sum[nums]) // 2 的方法数。
接下来的问题可以使用动态规划来解题，先建立数组，长度为temp+1，数组中每一个元素都代表的是和为下标时的方法数（dp[0]=1)，然后状态转移方程为
dp[i] += dp[i-num]。num是当前遍历到的数组的元素，最后返回dp[temp]即可。
"""
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # temp = sum(nums)
        # if S < -temp or S > temp:
        #     return 0
        # temp = S + sum(nums)
        # if temp % 2 == 1:
        #     return 0
        # temp //= 2
        # nums = filter(lambda x:x<=temp, nums)
        # # 这是字典
        # dp = dict()
        # dp[0] = 1
        # for num in nums:
        #     if num > temp:
        #         break
        #     for i in range(temp, num-1, -1):
        #         dp[i] = dp.get(i, 0) + dp.get(i-num, 0)
        # 下面用数组
        # dp = [0] * (temp+1)
        # dp[0] = 1
        # for num in nums:
        #     if num > temp:
        #         break
        #     for i in range(temp, num-1, -1):
        #         dp[i] += dp[i-num]
        # return dp[temp]

        # 下面的解法我感觉是最快的
        S += sum(nums)
        print(S)
        if S % 2 or S // 2 > sum(nums):
            return 0
        print('continue')
        S //= 2
        nums = list(filter(lambda x: x <= S, nums))
        dp = [0] * (S + 1)
        dp[0] = 1
        for num in nums:
            for i in range(S, num-1, -1):
                dp[i] += dp[i-num]
                print(dp[i], dp[i-num])
        print(dp)
        return dp[S]


solve = Solution()
# nums = [1,1,1,1,1]
# S = 3
# nums = [1,2,7,9,981]
# S = 1000000000
nums = [1]
S = 1
print(solve.findTargetSumWays(nums, S))