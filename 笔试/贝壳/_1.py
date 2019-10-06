n, S = map(int, input().strip().split(" "))
c = list(map(int, input().strip().split(" ")))
c.sort()
ret = 0
for num in c:
    S -= num
    if S >= 0:
        ret += 1
    if S < 0:
        break
print(ret)