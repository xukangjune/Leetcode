"""
我承认比较笨，用的很笨的方法，即动态规划。首先建立动态数组，数组中的每一项都是一个小数组，小数组的第一项代表的是本位置之前进行一次交易的值。
首先记录下进行一次交易的最大结果值，然后在遍历时，如果当前值小于前面的值，说明这个位置上第一次交易的结果之间不用计算，交易也是亏钱，所以直接
赋值为前面位置中最大的一次交易值。如果当前的值小于前面出现的最小的值，那么最小值重新赋值。如果当前值得到的一次交易收益大于记录的一次最大的一次
交易收益，那么一次交易收益重新赋值。
关于第二次交易，小数组寸的第二项为当前位置第二次交易值。由于只允许两次交易，那么从当前位置向前遍历，每遍历到一个位置，都要将遍历前一个位置的
一次交易值加到结果上，凑成两次交易。
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        if prices:
            lowestPrice = prices[0]
            n = len(prices)
            dp = [[0, 0] for i in range(n)]
            dp[0] = [0, 0]
            maxSingleTime = 0
            maxDoubleTime = 0
            for i in range(1, n):
                if prices[i] <= lowestPrice:
                    lowestPrice = prices[i]
                    dp[i][0] = maxSingleTime
                    dp[i][1] = maxDoubleTime
                    continue
                if prices[i] - lowestPrice > maxSingleTime:
                    maxSingleTime = prices[i] - lowestPrice
                dp[i][0] = maxSingleTime
                for j in range(1, i):
                    if prices[i] > prices[j]:
                        dp[i][1] = max(prices[i] - prices[j] + dp[j - 1][0], dp[i][1])
                        maxDoubleTime = max(dp[i][1], maxDoubleTime)
            ret = max(maxSingleTime, maxDoubleTime)
            print(dp)
            print(maxSingleTime)

        return ret


solve = Solution()
prices = [3,3,5,0,0,3,1,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [3,2,6,5,0,3]
print(solve.maxProfit(prices))