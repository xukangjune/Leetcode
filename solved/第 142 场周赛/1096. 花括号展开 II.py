class Solution:
    def braceExpansionII(self, expression: str):
        ret = []
        stack = []
        for char in expression:
            if char == '{':
                stack.append(char)
            elif char.isalpha():
                if stack and stack[-1].isalpha():
                    stack[-1] += char
                else:
                    stack.append(char)
            elif char == ',':
                stack.append(char)
            elif char == '}':
                temp = []
                while stack and stack[-1] != '{':
                    if stack[-1].isalpha():
                        temp.insert(0, stack[-1])
                    stack.pop()
                stack.pop()
                if temp:
                    if stack and stack[-1].isalpha():
                        temp = [stack[-1] + k for k in temp]
                        stack.pop()
                    if stack and stack[-1] == ',':
                        temp = ret + temp
                        stack.pop()
                    elif ret:
                        temp = [i + j for i in ret for j in temp]
                    ret = temp
        return sorted(list(set(ret)))


solve = Solution()
# s = "{a,b}{c{d,e}}"
# s = "{{a,z}, a{b,c}, {ab,z}}"
# s = "{a,b,c}"
# s = "{ab}"
# s = "{a,b},{b,c}"
# s = "{a,b}{c,d}"
# s = "a{b,c,d}"
# s = "{a{b,c}}{{d,e}f{g,h}}"
s = "{}"
print(solve.braceExpansionII(s))