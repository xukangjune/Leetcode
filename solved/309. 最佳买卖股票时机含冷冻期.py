"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75927/Share-my-thinking-process
目前想通了一点，留着以后继续思考。
"""
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
            print(sell, buy, prev_sell, prev_buy)
        return sell


solve = Solution()
# a = [0,1,0,1,0,1,0,1]
# a = [1,0,1,0,0,1]
# a = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
# a = [6,1,3,2,4,7]
a = [1,2,3,4,5,6]
print(solve.maxProfit(a))