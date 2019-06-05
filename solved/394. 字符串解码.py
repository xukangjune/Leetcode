"""
以前做过，直接用栈
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char!= '[':
                stack.append(char)
            else:
                tempStr = ''
                while stack[-1].isalpha():
                    tempStr = stack.pop() + tempStr
                stack.pop()
                tempNum = ''
                while stack and stack[-1].isdigit():
                    tempNum = stack.pop() + tempNum
                tempNum = '1' if not tempNum else tempNum
                for i in int(tempNum) * tempStr:
                    stack.append(i)
        return ''.join(stack)


solve = Solution()
s = "[abc]0[cd]ef"
print(solve.decodeString(s))