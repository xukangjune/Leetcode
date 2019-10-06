n = int(input().strip())
ret = []
expr = input().strip().split(' ')


stack = []

i = 0
tmp = []
pos = 0

if n == 1:
    print(' '.join(expr))
else:
    prev = expr[1]
    expr.append('$')
    while i < n:
        if expr[2 * i + 1] != prev:
            if expr[2 * i + 1] in "*/":
                for j in range(pos, 2 * i - 1):
                    if j % 2 == 0:
                        tmp.append(expr[j])
                pos = 2 * i
            else:
                for j in range(pos, 2 * i + 1):
                    if j % 2 == 0:
                        tmp.append(expr[j])
                pos = 2 * i + 2

            if prev in "/-":
                tmp = list(tmp[0]) + sorted(tmp[1:], key=lambda x: int(x))
            else:
                tmp.sort(key=lambda x: int(x))

            stack.extend(tmp)

            prev = expr[2 * i + 1]
            tmp = []

        i += 1

    for index, num in enumerate(stack):
        expr[2 * index] = num

    expr.pop()
    print(' '.join(expr))


