n = int(input().strip())
a = [i for i in range(n)]
i = 0
tmp = 1

while n != 1:
    if tmp % 5 == 0:
        print(a[i])
        del a[i]
        if i == n-1:
            i = 0
        n -= 1
        tmp = 1
    else:
        tmp += 1
        i += 1
        if i >= n:
            i = 0

print(a)


