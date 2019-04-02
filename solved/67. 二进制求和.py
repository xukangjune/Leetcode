"""
这一比较简单，我只自己写了一个二进制与十进制的转换，如果直接使用bin（）函数则也太简单了。
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '0' and b == '0':
            return str(0)
        i = 0
        j = 0
        num_a = 0
        num_b = 0
        ret = ''
        for char in a[::-1]:
            num_a += int(char) * 2 ** i
            i += 1
        for char in b[::-1]:
            num_b += int(char) * 2 ** j
            j += 1
        num = num_a + num_b
        while num != 0:
            ret = str(num % 2) + ret
            num //= 2
        return ret



solve = Solution()
a = '0'
b = '0'
print(type(solve.addBinary(a, b)))