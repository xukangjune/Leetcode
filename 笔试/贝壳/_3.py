n, m = map(int, input().strip().split(" "))
ret = 0

for i in range(n):
    x, y = map(int, input().strip().split(" "))
    if m < y:
        continue
    num = min(m // y, x)
    ret += num
    m -= y * num
    if m == 0:
        break
print(ret)