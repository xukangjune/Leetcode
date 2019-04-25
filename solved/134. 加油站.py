"""
第一种解法是自己写的，有点慢，最后一个例子超时了。
后来参考了网上的写法，遍历一次数组。首先将开始的起点设为0，并从0开始向后累加每次油箱剩余的油量，如果大于等于0，继续向后遍历；如果小于零，那么说明从
当前的起点到这里是行不通的，而且当前起点与当前点之间的所有点都不能到当前点（说明这两点之间都不是起点，贪心），所以下一个起点就取当前点的下一个点，并将
累加的油箱重置为零，并接着上面的做法。因为题目确定有解，那么上述的结果一定存在。
"""
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1
        n = len(gas)
        rest = 0
        ret = 0
        for i in range(n):
            rest += gas[i] - cost[i]
            if rest < 0:
                ret = i+1
                rest = 0
        return ret



        # 第一种解法，太慢，通过不了
        # dp = {}
        # n = len(gas)
        # for i in range(n):
        #     dp[i] = gas[i] - cost[i]
        # print(dp)
        # for i in dp.keys():
        #     if dp[i] < 0:
        #         continue
        #     j = i+1
        #     tempGas = dp[i]
        #     while j % n != i:
        #         tempGas += dp[j % n]
        #         if tempGas < 0:
        #             break
        #         j += 1
        #     if j % n == i:
        #         return j % n


solve = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
# gas  = [2,3,4]
# cost = [3,4,3]
# gas = [5,8,2,8]
# cost = [6,5,6,6]
print(solve.canCompleteCircuit(gas, cost))
