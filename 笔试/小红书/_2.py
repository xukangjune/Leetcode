str = input().strip()
stack = []
n = len(str)
i = 0
while i < n:
    if str[i].isalpha():
        if stack != [] and stack[-1] == '(':
            pass
        else:
            stack.append(str[i])

    elif str[i] == '<':
        if stack != [] and stack[-1] == '(':
            pass
        elif stack != []:
            stack.pop()

    elif str[i] == '(':
        stack.append('(')

    elif str[i] == ')':
        stack.pop()

    i += 1

print(''.join(stack))




