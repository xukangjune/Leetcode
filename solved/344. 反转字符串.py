"""
Python字符串是常量，所以不能直接操作，所以先转化成数组在进行交换操作。
"""
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        first = 0
        last = len(s) - 1
        while first < last:
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1
        return ''.join(s)


solve = Solution()
s = "A man, a plan, a canal: Panama"
print(solve.reverseString(s))
