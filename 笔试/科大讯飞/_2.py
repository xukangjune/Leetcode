line = input().strip().split(',')

count = 0
for str in line:
    if str.isdigit() and len(str) > 1 and int(str[0]) + int(str[-1]) > 8:
        count+= 1
print(count)