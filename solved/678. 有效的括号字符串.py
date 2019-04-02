"""
用的栈，速度还可以但是空间消耗比较大。
"""
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # leftBrackets, stars = 0, 0
        # for char in s[::-1]:
        #     if char == '(':
        #         leftBrackets += 1
        #     elif char == '*':
        #         stars += 1
        #     else:
        #         if leftBrackets:
        #             leftBrackets -= 1
        #         elif stars:
        #             stars -= 1
        #         else:
        #             return False
        # return stars >= leftBrackets

        stack = []
        for char in s:
            if char in '(*':
                stack.append(char)
            else:
                if stack:
                    i = len(stack)-1
                    while i > -1 and stack[i] != '(':
                        i -= 1
                    if i > -1:
                        del stack[i]
                    else:
                        del stack[-1]
                else:
                    return False
        stars = 0
        for char in stack[::-1]:
            if char == '*':
                stars += 1
            else:
                if stars:
                    stars -= 1
                else:
                    return False
        return True





solve = Solution()
s = "()"
# s = "((((*))"
# s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
print(solve.checkValidString(s))