line = input().strip()

stack=[]
for char in line:
    if char == ']':
        tmpStr = ''
        tmpNum = ''
        while stack and stack[-1] != '[':
            tmpStr = stack.pop() + tmpStr
        stack.pop()
        while stack and stack[-1].isdigit():
            tmpNum = stack.pop() + tmpNum
        tmpStr *= int(tmpNum)
        for tmpChar in tmpStr:
            stack.append(tmpChar)
    else:
        stack.append(char)

print(''.join(stack))
