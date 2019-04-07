"""
我自己写的比较拖沓，原本是想准备两个数组来存储原数组每一位左边的数累积和右边的数累积，到那时这样就不满足题意了。因为返回
数组不计入额外空间，所以这个条件可以利用。所以我就将左边数的累积计算到返回数组，然后将反向乘上右边数的累积。
新的解法比较流畅，只需要两遍遍历数组，只需要两个遍历来记录当前左边和右边数累乘的结果。
"""
class Solution:
    def productExceptSelf(self, nums):
        #新的解法
        n = len(nums)
        ret = [1] * n
        left = 1
        for i in range(n):
            ret[i] *= left
            left *= nums[i]    #此时的ret为nums每一位前面所有数的乘积，不包括自己

        right = 1
        for i in range(n-1, -1, -1):
            ret[i] *= right
            right *= nums[i]   #同上面的思路相同，此时的right代表每一位右边所有的数相乘
        return ret

        # 原本的解法，满足要求但是有点拖沓
        # n = len(nums)
        # ret = [1] * n
        # left = 1
        # for i, num in enumerate(nums):
        #     if i == 0:
        #         ret[0] = num
        #     else:
        #         ret[i] = num * ret[i-1]
        # post = 1
        # for i in range(n-1, 0, -1):
        #     ret[i] = ret[i-1] * post
        #     post *= nums[i]
        # ret[0] = post
        # return ret


solve = Solution()
nums = [1,2, 3, 4]
print(solve.productExceptSelf(nums))