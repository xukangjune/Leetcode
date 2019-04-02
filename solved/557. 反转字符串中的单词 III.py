"""
我感觉用字符串的方法函数虽然很快，但是有点作弊的嫌疑，我还是遍历字符串慢慢来（真的很慢😔）。没啥特别的。就是最后返回ret时要注意加上temp。
因为最后一个单词遍历完后，由于后面没有空格，所以不执行else语句，因此要手动加上去。
"""
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        temp = ''
        for char in s:
            print(char)
            if char != ' ':
                temp = char + temp
            else:
                temp += char
                ret += temp
                temp = ''
        return ret + temp


solve = Solution()
s = ''
print(solve.reverseWords(s))