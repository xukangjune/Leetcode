"""
不知道这题的意图是什么，反正我用的时最复杂的方法，将每个字符串的字符转成数字，然后逐个相乘。然后再相加。
哦，看懂了。好一点的方法就是先建立一个数组（数组的长度就是就是最长的数的长度，然后遍历短一点的数，数组中记录的是长字符串
数字每一位出现的次数。最后累加
"""
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # if num1 == '0' or num2 == '0':
        #     return '0'
        # if num1 == '1':
        #     return num2
        # if num2 == '1':
        #     return num1
        # if len(num2) < len(num1):
        #     num1, num2 = num2, num1
        # n = len(num1)
        # ret = '0'
        #
        # def mulstrings(factor):
        #     nums = ''
        #     carry = 0
        #     for num in num2[::-1]:
        #         num = int(num)
        #         res = num * int(factor) + carry
        #         nums = str(res % 10) + nums
        #         carry = res // 10
        #     if carry:
        #         nums = str(carry) + nums
        #     return nums
        #
        # def addStrings(num1, num2):
        #     carry = 0
        #     if len(num1) < len(num2):
        #         num1, num2 = num2, num1
        #     ret = ''
        #     i = -1
        #     length = -len(num2)
        #     while i >= length:
        #         num = int(num1[i]) + int(num2[i]) + carry
        #         ret = str(num % 10) + ret
        #         carry = num // 10
        #         i -= 1
        #     if not carry:
        #         return num1[:i + 1] + ret
        #     length = -len(num1)
        #     while i >= length and carry:
        #         num = int(num1[i]) + carry
        #         ret = str(num % 10) + ret
        #         carry = num // 10
        #         i -= 1
        #     if not carry:
        #         return num1[:i + 1] + ret
        #     return '1' + ret
        #
        # for i in range(n-1, -1, -1):
        #     zeros = n-1 - i
        #     if num1[i] != '0':
        #         res = mulstrings(num1[i])
        #         res += '0' * zeros
        #         ret = addStrings(ret, res)
        # return ret

        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1
        num1 = list(map(int, num1))
        num2 = list(map(int, num2))
        n1 = len(num1)
        n2 = len(num2)
        ret = [0] * (n1+n2-1)
        print(n1, n2)
        for i in range(n2):
            for j in range(n1):
                ret[i+j] += num1[j] * num2[i]
        carry = 0
        for i in range(n1+n2-2, -1, -1):
            ret[i] += carry
            carry = ret[i] // 10
            ret[i] %= 10
        return str(carry)+''.join(str(num) for num in ret) if carry else ''.join(str(num) for num in ret)


solve = Solution()
num1 = "123456"
num2 = "456"
print(solve.multiply(num1, num2))