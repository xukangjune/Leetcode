"""
动态规划的结果比较慢，而且内存消耗大
"""
class Solution:
    def coinChange(self, coins, amount):
        # 动态规划
        if amount == 0:
            return 0
        dp = [1000] * (amount+1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, amount+1):
            if dp[i] != 1:
                temp = [dp[i - coin] for coin in coins if coin <= i]
                if temp:
                    dp[i] = 1 + min(temp)
        print(dp)
        return dp[amount] if dp[amount] < 1000 else -1

        # dfs, 我写的太慢了
        # if amount == 0:
        #     return 0
        # coins.sort()
        # n = len(coins)-1
        # print(coins)
        #
        # def dfs(target, lastIndex):
        #     ret = 1000
        #     if lastIndex == -1:
        #         return 1000
        #     if lastIndex == 0:
        #         if target % coins[lastIndex]:
        #             return ret
        #         return target // coins[lastIndex]
        #     maxFactor = target // coins[lastIndex]
        #     if maxFactor:
        #         if target % coins[lastIndex] == 0:
        #             return maxFactor
        #         for i in range(maxFactor, -1, -1):
        #             res = dfs(target-coins[lastIndex]*i, lastIndex-1)
        #             ret = min(i+res, ret)
        #     else:
        #         return dfs(target, lastIndex-1)
        #     return ret
        #
        # ret = dfs(amount, n)
        # return ret if ret < 1000 else -1


solve = Solution()
# coins = [1, 2, 5]
# amount = 11
# coins = []
# amount = 1
# coins = [186,419,83,408]
# amount = 6249
coins = [438,86,218,138,358,152,129]
amount = 7656
print(solve.coinChange(coins, amount))