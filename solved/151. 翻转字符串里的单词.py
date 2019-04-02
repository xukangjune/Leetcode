"""
这一题比较简单，用到了字符串的几个方法（但我不确定，考的是不是这个方向）。
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 这中方法完全就是投机取巧，感觉并不是题目要考的内容
        # s = s.split()
        # return ' '.join(s[::-1])

        # 下面的这个方法
        ret = []
        temp = ''
        for char in s:
            if char != ' ':
                temp += char
                continue
            else:
                if temp:
                    ret.append(temp)
                    temp = ''
        print(ret, temp)
        if temp:
            ret.append(temp)
        return ' '.join(ret[::-1])



solve = Solution()
s = "  the sky is  blue"
print(solve.reverseWords(s))