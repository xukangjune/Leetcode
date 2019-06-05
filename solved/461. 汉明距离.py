"""
先异或，循环统计最右边1的个数，后右移。
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        ret = 0
        while temp:
            ret += (temp & 1)
            temp >>= 1
        return ret


solve = Solution()
print(solve.hammingDistance(3, 4))