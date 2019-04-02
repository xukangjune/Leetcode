class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ''
        # 方法太笨了
        # dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
        #         10: 'X', 20: 'XX', 30: 'XXX',40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
        #         100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
        #         1000: 'M', 2000: 'MM', 3000: 'MMM'}
        # i = 10
        # while num != 0:
        #     temp = num % i
        #     if temp in dict:
        #         ret = dict[temp] + ret
        #     num -= temp
        #     i *= 10
        #     print(num, i)
        # return ret

        while num > 0:
            if num >= 1000:
                ret += 'M'
                num -= 1000
            elif num >= 100:
                if num >= 900:
                    ret += 'CM'
                    num -= 900
                elif num >= 500:
                    ret += 'D'
                    num -= 500
                elif num >= 400:
                    ret += 'CD'
                    num -= 400
                else:
                    ret += 'C'
                    num -= 100
            elif num >= 10:
                if num >= 90:
                    ret += 'XC'
                    num -= 90
                elif num >= 50:
                    ret += 'L'
                    num -= 50
                elif num >= 40:
                    ret += 'XL'
                    num -= 40
                else:
                    ret += 'X'
                    num -= 10
            else:
                if num == 9:
                    ret += 'IX'
                    break
                elif num >= 5:
                    ret += 'V'
                    num -= 5
                elif num == 4:
                    ret += 'IV'
                    break
                else:
                    ret += 'I'
                    num -= 1
        return ret




solve = Solution()
print(solve.intToRoman(40))