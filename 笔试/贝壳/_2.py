n, k = map(int, input().strip().split(" "))
t = input().strip()
ret = t * k
for i in range(1, n):
    src = t[i:]
    des = t[:n-i]
    if src == des:
        ret = t + t[n-i:] * (k-1)
        break
print(ret)
