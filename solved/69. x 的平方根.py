"""
数学不行呀！！！！
"""
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 虽然通过了，但是非常慢
        # i = 1
        # while i * i <= x:
        #     i += 1
        # return i- 1

        # 采用牛顿迭代法
        # if x <= 1:
        #     return x
        # a = x
        # while a * a > x:
        #     a = (a + x / a) // 2
        # return int(a)

        # 二分法
        if x <= 1:
            return x
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1



solve = Solution()
print(solve.mySqrt(100))