"""
以前遇到的位运算的方法忘记了，我自己用的方法虽然也比较简单直观，但是没有创新性。后来看到位运算觉得很棒。首先k&k-1就是将k二进制右边的1去除了，那么
只要将与运算得到的数二进制1的个数加上1就是k的1的个数，非常号的解法。
"""
class Solution:
    def countBits(self, num: int):
        ret = [0] * (num+1)
        for k in range(1, num+1):
            ret[k] = 1 + ret[k & (k-1)]
        return ret

        # 中规中矩的方法，没有给面试官带来惊喜
        # ret = [0]
        # n = 1
        # while 2 ** n - 1 < num:
        #     ret += [1+i for i in ret]
        #     n += 1
        # ret += [1+i for i in ret[:num-2**(n-1)+1]]
        # return ret


solve = Solution()
print(solve.countBits(5))