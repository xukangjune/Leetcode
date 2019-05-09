"""
比较简单的题目，直接用栈据可以解题。主要的问题是关于负数的除法。
"""
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in "+-*/":
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left+right)
                elif token == '-':
                    stack.append(left-right)
                elif token == '*':
                    stack.append(left*right)
                else:
                    stack.append(int(left/right))
            else:
                stack.append(int(token))
        return stack[0]


solve = Solution()
s = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# s = ["4","-2","/","2","-3","-","-"]
print(solve.evalRPN(s))