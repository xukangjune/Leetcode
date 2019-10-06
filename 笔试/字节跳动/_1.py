
N = int(input().strip())
tmp = [i for i in range(N)]
ret = N

def find_parent(x):
    if tmp[x] != x:
        return find_parent(tmp[x])
    else:
        return x


for i in range(N):
    grid = list(map(int, input().strip().split(" ")))
    for j in range(i+1, N):
        if grid[j] >= 3:
            if find_parent(i) != find_parent(j):
                ret -= 1
                while tmp[j] != j:
                    j, tmp[j] = tmp[j], i
                tmp[j] = i
print(ret)



