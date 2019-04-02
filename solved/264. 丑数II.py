"""
这题是找出第n个丑数，我的方法用到了集合，并在集合与数组之间转化，比较慢
最好的方法应用到了数学知识。
"""
class Solution(object):
    n = 1690
    listSet = {1}
    index = 0
    while n != 1:
        ret = sorted(list(listSet))[index]
        new = {ret * 2, ret * 3, ret * 5}
        listSet |= new
        index += 1
        n -= 1
    listSet.add(1)
    ret = sorted(list(listSet))

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ret[n-1]


        # return sorted([2**a * 3**b * 5**c for a in range(5) for b in range(5) for c in range(5)])[n-1]

solve = Solution()
print(solve.nthUglyNumber(1690))
