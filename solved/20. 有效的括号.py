"""
经典习题，用栈的思想，直接可以用数组来替代。
"""
class Solution:
    brackets = {')': '(', '}': '{', ']': '['}
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ret = []
        for char in s:
            if char in '{[(':
                ret.append(char)
            else:
                if not ret or ret.pop() != self.brackets[char]:
                    return False
        return not ret


solve = Solution()
# s = "()[]{}"
# s = "(]"
# s = "([)]"
s = "]"
# s = "["
print(solve.isValid(s))