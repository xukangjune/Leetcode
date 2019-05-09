"""
这题很有趣，希纳是用自己的dfs方法，但是超时了，后来看见别人的思路，尝试用dp来解题（背包问题），最后虽然解出来了，但是还是比较slow（800多ms）。
然后看了前几名的答案，发现他们用的也是dfs，和我第一题的思路相同，但是用的是降序的dfs。
关于nums的顺序很重要，我开始用的是升序，所以每次从target中拿去的数很小，容易超时，后来改成降序后，每次从target拿去的数都比较大，所以dfs递归的很快，
有点贪心的意思。所以以后做题的时候尽可能的在每一步操作中获取最大的利益。
"""
class Solution:
    def canPartition(self, nums):
        # 这是我自己写的dfs，使用递归，开始用的升序nums，后来改成了降序nums，快了很多。
        nums.sort(reverse=True)
        total = sum(nums)
        if total % 2 or nums[-1] * 2 > total:
            return False
        target = total // 2
        n = len(nums)

        def dfs(i, target):
            if target == 0:
                return True
            while i < n:
                if target < nums[i]:
                    return False
                if dfs(i+1, target-nums[i]):
                    return True
                i += 1
            return False

        return dfs(0, target)

        # 这是看的别人的思路，动态规划
        # total = sum(nums)
        # if total % 2 or nums[-1] * 2 > total:
        #     return False
        # target = total // 2
        # print(target)
        # dp = [0] * (target+1)
        # dp[0] = 1
        #
        # for num in nums:
        #     for i in range(target, num-1, -1):
        #         dp[i] = dp[i-num] or dp[i]
        # return dp[target]

solve = Solution()
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,97,95]
print(solve.canPartition(nums))