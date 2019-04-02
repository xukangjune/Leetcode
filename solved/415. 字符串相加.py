"""
本题就两个字符串的和，从最后开始依次向前遍历，需要注意的是局势当一个字符串遍历完后，另外一个字符串的情况，没什么重要的了。
"""
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        ret = ''
        i = -1
        length = -len(num2)
        print(num1, num2, length)
        while i >= length:
            num = int(num1[i]) + int(num2[i]) + carry
            ret = str(num % 10) + ret
            carry = num // 10
            i -= 1
        print(i)
        if not carry:
            print(num1[:i])
            return num1[:i+1] + ret
        length = -len(num1)
        while i >= length and carry:
            num = int(num1[i]) + carry
            ret = str(num % 10) + ret
            carry = num // 10
            i -= 1
        print(i)
        if not carry:
            return num1[:i + 1] + ret
        print()
        return '1' + ret



solve = Solution()
num1 = '19'
num2 = '31'
print(solve.addStrings(num1, num2))