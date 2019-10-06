n, m = map(int, input().strip().split(" "))
tree = [0] * n
ret = 0
for _ in range(m):
    a, b = map(int, input().strip().split(" "))
    for i in range(a-1, b):
        if not tree[i]:
            tree[i] = 1
            ret += 1
    print(ret)


