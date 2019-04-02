"""
字符串的几个方法要记得，isalnum（）是直接判断是否是字母或者字母。然后字符串由于是常量，所以使用方法后也生成的是新的字符串。
"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(char.lower() for char in s if char.isalnum())
        first = 0
        last = len(s) -1
        while first < last:
            if s[first] == s[last]:
                first += 1
                last -= 1
            else:
                return False
        return True


solve = Solution()
s = "A man, a plan, a canal: Panama"
print(solve.isPalindrome(s))