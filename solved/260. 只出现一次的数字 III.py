"""
这个题目很经典。只有两个数不同，那么这两个数异或结果的二进制形式中，出现1的位置说就说明这个两个数在此位置上二进制不相同。
那么取出最右边一个1的位置，有很快的解法，就是将原数与取反后的数做与运算，结果最为mask，来与所有的数做与运算。所有在此位置
为1包括两个不同数中的一个都可以划分到一边，其余的数在另一组，然后各组进行异或运算，得到的结果就是两个要求的数。
"""
from functools import reduce
from operator import xor
class Solution:
    def singleNumber(self, nums):
        temp = reduce(xor, nums)
        mask = temp & (-temp)
        ret = [0] * 2
        for num in nums:
            if num & mask:
                ret[0] ^= num
            else:
                ret[1] ^= num
        return ret


solve = Solution()
nums = [1,2,1,3,2,5]
print(solve.singleNumber(nums))