def climb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        first = 1
        second = 2
        third = 4
        tmp = 0
        for i in range(4, n+1):
            tmp = first + second + third
            first, second, third = second, third, tmp
        return tmp

a = int(input())
print(climb(a))