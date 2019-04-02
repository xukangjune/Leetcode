"""
本题将罗马数字转为阿拉伯数字，其实在于IXC这三个数出现时，是加上还是减去。只要在遇到这些字母时，看后一位的字母是什么，就可以判断了。
别人用的是字典要快很多。
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        num = 0
        # 第一种解法，有点慢
        # for i in range(length):
        #     if s[i] == 'I':
        #         num += -1 if i + 1 < length and s[i+1] in 'VX' else 1
        #     elif s[i] == 'X':
        #         num += -10 if i + 1 < length and s[i + 1] in 'LC' else 10
        #     elif s[i] == "C":
        #         num += -100 if i + 1 < length and s[i + 1] in 'DM' else 100
        #     elif s[i] == 'V':
        #         num += 5
        #     elif s[i] == 'L':
        #         num += 50
        #     elif s[i] == 'D':
        #         num += 500
        #     else:
        #         num += 1000
        # return num

        # 第二种解法，使用字典，而且对遍历的中止条件有所调整。
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        for i in range(length-1):
            num += -dict[s[i]] if dict[s[i]] < dict[s[i+1]] else dict[s[i]]
        return num + dict[s[length-1]]

solve = Solution()
s = "MCMXCIV"
print(solve.romanToInt(s))