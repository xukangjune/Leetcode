# coding=gbk
class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        for i in range(n-1, 1, -1):
            if n % i == 0:
                return self.minSteps(i) + (n // i)
        return n

