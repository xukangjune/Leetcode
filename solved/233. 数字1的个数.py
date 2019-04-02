"""
本题主要考察数学基础。其实从000...000~999...999这期间1出现的次数是所有数字的总和的10分之1。这点知道就够了。计算位数可以先转化为字符串，
这样使用字符串的方法就好求多了。
"""
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 太慢了
        # 算了，也还行吧
        ret = 0
        if n <= 0:
            return ret
        n = str(n)
        length = len(n)
        if n[length-1] > '0':
            ret += 1
        for i in range(length-1):
            if n[i] > '1':
                ret += 10 ** (length - i - 1)
                ret += int(n[i]) * (length - i - 1) * 10 ** (length - i - 2)
            elif n[i] == '1':
                ret += 1
                ret += int(n[i+1:])
                ret += int(n[i]) * (length - i - 1) * 10 ** (length - i - 2)
        return ret


solve = Solution()
print(solve.countDigitOne(1))