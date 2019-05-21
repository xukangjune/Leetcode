"""
位运算解题。解法非常巧妙。首先先判断m是不是零，如果是的话，好办直接返回0。如果不是那么就先判断m与n是否相等，如果不相等，那么从m到n一定有一个正数和
一个负数（至少），那么从二进制的角度来看，二进制的m到n的最后一位一定（至少）有一个0，那么的话，最后一位此时相与一定是0，所以先设定一个计数值count，
m，n不等是，count自增1，并且m和n都右移一位，然后循环判断m与n是否相等。如果m=n时，退出循环。m=n，说明此时m，n相与还是m，所以最后的结果就是m左移
count位。
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        count = 0
        while m != n:
            count += 1
            m >>= 1
            n >>= 1
        return m << count


solve = Solution()
print(solve.rangeBitwiseAnd(0, 1))