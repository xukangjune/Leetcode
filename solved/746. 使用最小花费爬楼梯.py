"""
本题使用动态规划，从后向前遍历
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 我的方法，还不是最快的
        # length = len(cost)
        # if length > 2:
        #     for i in range(length-3, -1, -1):
        #         cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2])
        # return min(cost[0], cost[1])

        # 根据别人的方法，应该会快一点
        a = cost[-1]
        b = cost[-2]
        for i in cost[-3::-1]:
            b, a = i+min(b, a), b
        return min(a, b)




solve = Solution()
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost = [10, 15]
print(solve.minCostClimbingStairs(cost))
print(cost)