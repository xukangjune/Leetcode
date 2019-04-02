class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # stairsList = [0] * n
        # stairsList[1] = 1
        # stairsList[2] = 2
        # i = 3
        # while i < n:
        #     stairsList[i] = stairsList[i-1] + stairsList[i-2]
        #     i += 1
        # return stairsList[n-2] + stairsList[n-1]

        f1 = 1
        f2 = 1
        f3 = 0
        if n == 1:
            return f1
        i = 2
        while i < n+1:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            i += 1
        return f3


solve = Solution()
print(solve.climbStairs(2))