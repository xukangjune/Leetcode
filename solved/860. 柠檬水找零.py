"""
我用了字典，其实并不需要字典，只要设定两个遍历代表5和10的个数就OK了。
"""
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dict = {}
        dict[5] = 0
        dict[10] = 0
        for money in bills:
            if money == 5:
                dict[5] += 1
            elif money == 10:
                if dict[5] > 0:
                    dict[5] -= 1
                    dict[10] += 1
                else:
                    return False
            else:
                if dict[10] > 0 and dict[5] > 0:
                    dict[10] -= 1
                    dict[5] -= 1
                elif dict[5] > 2:
                    dict[5] -= 3
                else:
                    return False
            print(dict)
        return True


solve = Solution()
# bills = [5,5,10]
# bills = [5,5,10,10,20]
# bills = [5,5,5,5,20,20,5,5,20,5]
bills = [5,5,20,5,5,10,5,10,5,20]
print(solve.lemonadeChange(bills))