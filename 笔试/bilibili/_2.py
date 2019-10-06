n = int(input().strip())

if n <= 2:
    print(1)
else:
    ret = 0
    for i in range(1, n+1):
        m = n - i*(i-1)/2
        if m <= 0:
            break
        if m%i == 0:
            ret += 1

    print(ret)