"""
此题关键就是先将字符串尾的空格先去除，第一种方法是字符串的方法，第二种则是遍历字符串。总的来说第二种方法占用的内存应该小一点。
"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 感觉我这种方法有点不妥，感觉在投机取巧
        # s = s.rstrip(' ')
        # ret = 0
        # for char in s[::-1]:
        #     if char == ' ':
        #         return ret
        #     ret += 1
        # return ret

        # 下面是网上的一个解法
        a, b = 0, len(s)-1
        while b >= 0 and s[b] == ' ':
            b -= 1
        while b >= 0 and s[b] != ' ':
            a += 1
            b -= 1
        return a


solve = Solution()
# s = "Hello World"
s = 'a '
print(solve.lengthOfLastWord(s))