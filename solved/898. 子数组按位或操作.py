"""
墙外的高手做的，看起来事平方的时间复杂度，事实上是31N，但不知道为什么，再好好想想。
想通了，每次遍历到一个数，都要将这个数与前面所有的结果做与运算。因为是与运算，只要某一位（二进制）上为1， 那么就会cur集合所有数的这一位就会全部为1，
所以有很大的概率导致集合数操作后出现重复的情况。事实上，所有最坏的情况是[0，1，2,4,8,16,32,64,...,2^29]，这样每次循环内，当前的数与cur里的数与运算
后不能消除掉一部分，导致cur的最后长度为31。
所以，总的来说，还是为线性复杂度。
"""
class Solution:
    def subarrayBitwiseORs(self, A):
        cur, res = set(), set()
        for i in A:
            cur = {i | j for j in cur}
            cur.add(i)
            res |= cur
        return len(res)


solve = Solution()
a = [1,1,4]
print(solve.subarrayBitwiseORs(a))