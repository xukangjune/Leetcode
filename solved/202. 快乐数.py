"""
这一题比较简单
"""
class Solution(object):
    bag = set()
    bag.add(1)
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        basket = set()
        if n in self.bag:
            return True
        while n != 1 and n not in basket and n not in self.bag:
            basket.add(n)
            temp = 0
            for i in str(n):
                temp += int(i) ** 2
            print(n)
            n = temp
        if n in basket:
            return False
        self.bag |= basket
        return True


solve = Solution()
print(solve.isHappy(17415286415241547845))