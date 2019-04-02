"""
本题是计算一个正整数最少能够被几个完全平方数求和。王少有个四平方定理，可以通过数学的手段来解此题。但是此题的目的是训练动态规划的思想。
可以通过自底向上的动态规划，先可以建立一个数组，范围可以大一点，这里选取10000.然后从一开始，逐个计算。这里如果是平方数就直接在字典里
存1，如果不是，先找出小于该数的最大平方数，开方后得到一个边界值。从1遍历到这个边界值，将待求数减去遍历值的平方，此时会得到一系列的值，
在字典里超出这些key，最小的value，然后加一，就是所求值的最小平方数。
"""
from math import sqrt
class Solution(object):
    dict = {}
    for i in range(1, 10000):
        if i < 4:
            dict[i] = i
        elif sqrt(i) % 1 == 0:
            dict[i] = 1
        else:
            temp = int(sqrt(i)) + 1
            min = i
            for j in range(1, temp):
                min = 1 + dict[i-j**2] if 1 + dict[i-j**2] < min else min
            dict[i] = min

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        print(self.dict)
        return self.dict[n]
        # if n in self.dict:
        #     return self.dict[n]
        # elif sqrt(n) % 1 == 0:
        #     self.dict[n] = 1
        #     return 1
        # else:
        #     temp = int(sqrt(n)) + 1
        #     new = 1 + min(self.numSquares(n - i ** 2) for i in range(1, temp))
        #     self.dict[n] = new
        #     return new


solve = Solution()
print(solve.numSquares(48))