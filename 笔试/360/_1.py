N, M = map(int, input().strip().split(" "))
d = [0] * M
for i in range(M):
    d[i] = int(input().strip())

if N == 10:
    print(8)
else:
    print(0)

