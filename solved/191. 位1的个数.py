"""
很简单的题目，直接用位运算解题，解法也比较多。
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n != 0:
            n &= (n-1)
            ret += 1
        return ret

        # while n != 0:
        #     if n & 1:
        #         ret += 1
        #     n >>= 1
        # return ret


solve = Solution()
print(solve.hammingWeight(0))