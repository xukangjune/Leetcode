"""
我用了比较常规的方法，遍历字符串t，然后贪心，如果找到了当前的s中的元素，就将当前s的位置加1。最后，如果s查找的范围超过等于
s的长度，返回True。t遍历完后，还要加一次判断i==n，才能确定是否为False。
比较快的解法，用了字符串的index方法或find方法。
"""
class Solution:
    def isSubsequence(self, s, t):
        if not s:
            return True
        n = len(s)
        i = 0
        for char in t:
            if i == n:
                return True
            if char == s[i]:
                i += 1
        return True if i== n else False


solve = Solution()
s = "b"
t = "dbf"
print(solve.isSubsequence(s,t))