
line = input().strip()
if not line:
    print([])
else:
    line1, line2 = line.split('|')

    num1 = []
    num2 = []
    if line1:
        num1 = list(map(int, line1.split(',')))
    if line2:
        num2 = list(map(int, line2.split(',')))

    num = num1 + num2

    print(sorted(list(set(num))))