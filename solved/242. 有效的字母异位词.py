"""
这竟然是一道微软的面试题！！！！（震惊脸）
解法很多，如果只考虑字母的话，可以直接申请一个26大小的数组，s中出现字母在数组上就加一，t中出现就减一，看最后数组的值是否全部为0。
还有的解法就是直接排序，看排序后的结果是否相等。
"""
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if s == t:
            return True
        temp = [0] * 26
        for i in range(len(s)):
            temp[ord(s[i]) - 97] += 1
            temp[ord(t[i]) - 97] -= 1
        return temp.count(0) == 26


solve = Solution()
s = "anagray"
t = "nagaram"
# s = '@%&一三五'
# t = '一@&五三%'
print(solve.isAnagram(s, t))