"""
这一题其实不难，为什么通过率这么低呢？因为测试的例子坑太多了。一定要考虑全面，比如出现负数，零，整数溢出等等。
我的办法先求取整数部分，此处要注意一点，那就是当整数部分没有时，要手动的添上0。还要手动写上小数点。关于小数循环的部分，首先用字典存储被除数每一位
在字符串的位置，当后面出现相同的被除数时，就会停止循环然后从字典中找到相应的位置，然后插入括号。
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0: return ''
        if numerator == 0: return '0'

        ret = []
        if numerator * denominator < 0:
            ret.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)

        map = dict()
        if numerator >= denominator:
            ret.append(str(numerator // denominator))
            numerator %= denominator

        if numerator:
            if not ret or ret[-1] == '-':
                ret.append('0')
            ret.append('.')
            i = len(ret)
            while numerator and numerator not in map:
                map[numerator] = i
                numerator *= 10
                ret.append(str(numerator // denominator))
                numerator %= denominator
                i += 1

        if numerator in map:
            ret.insert(map[numerator], '(')
            ret.append(')')

        return "".join(ret)


solve = Solution()
print(solve.fractionToDecimal(33, 111))
