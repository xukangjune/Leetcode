"""
挺简单的一道题，有一个坑就是costs数组不是递递增的，要注意！
我的方法占的内存挺小的，应该是我的动态数组长度不是366，而是视用例而定。
"""

class Solution:
    def mincostTickets(self, days, costs):
        dp = [float("inf")] * (days[-1]+1)
        dp[0] = 0
        days = set(days)
        for day in range(1, days[-1]+1):
            if day not in days:
                dp[day] = dp[day-1]
            else:
                temp1 = (dp[day - 1] if day - 1 >= 0 else 0) + costs[0]
                temp2 = (dp[day - 7] if day - 7 >= 0 else 0) + costs[1]
                temp3 = (dp[day - 30] if day - 30 >= 0 else 0) + costs[2]
                dp[day] = min(temp1, temp2, temp3)
        print(dp)
        return dp[-1]

solve = Solution()
# days = [1,2,3,4,5,6,7,8,9,10,30,31]
# costs = [2,7,15]
# days = [1,4,6,7,8,20]
# costs = [2,7,15]
days = [1,4,6,7,8,20]
costs = [7,2,15]
print(solve.mincostTickets(days, costs))