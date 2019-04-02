"""
本题是一个无序的列表，所以在开始先定义buy和ret，赋值为第一个数和零，接下来遍历列表。如果遍历的数减去buy大于ret，就赋值给ret，如果不是则
继续遍历，如果遍历的数小于buy，说明此刻买入更为划算，所以将此值赋给buy，并继续遍历。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        if prices == []:
            return ret
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
                continue
            ret = price - buy if price - buy > ret else ret
        return ret


solve = Solution()
prices = []
print(solve.maxProfit(prices))