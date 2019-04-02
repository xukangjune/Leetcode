"""
本体比较好的解法有两种，第一种采用移位操作，即记录下所有数字每一位所有的1的和，如果这些1的和是3的倍数，那么说明这些1所在的
数都是成三出现的，不予考虑。如果不是3的倍数，就说明多出来的1是单独的数提供的。只要此时将1的位置记录下来，然后移动到res上。
但是Python关于负数的左移和右移无法将负号去除，所以在此之前先要判断负数的个数是否是三的倍数，还要将所有的负数取绝对值。
另一个方法比较费脑子，数电学得好的人比较好解。其实对于一个出现三次的数，可以看成是一个计数器。写出状态方程，最后化简就可以
得到最终的结果（具体可以参考https://blog.csdn.net/qq_17550379/article/details/83926804，以及
https://blog.csdn.net/jiangxiewei/article/details/82227451）。
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Python移位操作有问题，左移一位就是直接乘以2，右移一位就是直接除以2。这样运算会连同符号为一起操作。
        # res = 0
        # for i in range(32):
        #     temp = 0
        #     count = 0
        #     for num in nums:
        #         if num < 0:
        #             count += 1
        #             num = -num
        #         temp += (num >> i) & 1
        #
        #     if temp % 3:
        #         res |= 1 << i
        #         print(temp, res)
        #
        # return -res if count % 3 else res

        # 看到的一个位运算来解题的，看了一晚上，总算有了点头绪
        a, b = 0, 0
        for num in nums:
            a = (a ^ num) & ~b
            b = (b ^ num) & ~a
        return a


solve = Solution()
# nums = [2,2,3,2,3,3,122]
nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
print(solve.singleNumber(nums))