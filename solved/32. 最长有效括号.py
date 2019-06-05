"""
原来不会做的题。我是这样做的，要想括号匹配，那么必须左右括号都得匹配。所以先建立一个栈，遇到左括号，对应的下标就入栈。遇到右括号时，如果栈不为空，说明
可以匹配成功。我的做法是暂时记录这个长度，即在建立的字典中，将右括号的下标作为键，当前匹配成功的长度为值。那么，当当前匹配成功时，检查当前匹配成功的左
括号前一位是否在字典内，如果在，说明匹配成功的括号长度变长，将得到的长度与返回值比较。这对于"()()()"这种情况是符合的。对于"((()))"这种情况，可以
得到外层的长度会比内层长度大，所以也是适合的。
"""
class Solution:
    def longestValidParentheses(self, s):
        stack = []
        right = dict()
        ret = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif stack:
                leftIndex = stack.pop()
                temp = i - leftIndex + 1
                if leftIndex - 1 in right:
                    temp += right[leftIndex-1]
                right[i] = temp
                ret = max(ret, temp)
        return ret







solve = Solution()
# s = "(()"
# s = ")()())"
# s = "))))()))))(())"
s = "()(()"
# s = "()()()()()()()()()()(())"
# print(len(s))
print(solve.longestValidParentheses(s))