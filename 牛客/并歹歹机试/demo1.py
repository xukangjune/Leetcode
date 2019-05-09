line = input()
stack = []
count = 0
for char in line:
    if len(stack) != 0 and stack[-1] == char:
        stack.pop()
        count += 1
    else:
        stack.append(char)
print(count)