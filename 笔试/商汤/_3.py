n, x = map(int, input().strip().split(" "))
l = n
r = x

while l>=r:
    mid = (l+r) // 2
    _n = 0
    _x = x
    tmp = 0
    while _x:
        p = _x % 10
        _n += p * mid ** tmp
        tmp += 1
        _x //= 10
    if _n == n:
        print(mid)
        break
    elif _n > n:
        l=mid-1
    else:
        r=mid+1

