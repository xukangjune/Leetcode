"""
这里还是用了双指针，从字符串头尾开始遍历，如果遇到不相等的地方，就退出遍历。然后在不相等的地方可能会出现两种情况，即选择删除哪一个字符，所以
这里就要分两种情况。两种情况分别考虑，如果两种情况中都又出现了不相等的情况，就输出False。如果在其中一种情况中出现了遍历完字符串的情况，说明可
以删除一个字符完成回文字符串，输出True。
"""
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        first = 0
        last = n-1
        while first < last:
            if s[first] != s[last]:
                break
            first += 1
            last -= 1
        if first >= last:
            return True
        a = first
        b = last-1
        while a < b:
            if s[a] != s[b]:
                break
            a += 1
            b -= 1
        if a >= b:
            return True
        a = first + 1
        b = last
        while a < b:
            if s[a] != s[b]:
                break
            a += 1
            b -= 1
        if a >= b:
            return True
        return False


solve = Solution()
s = "abcdgedgcba"
print(solve.validPalindrome(s))