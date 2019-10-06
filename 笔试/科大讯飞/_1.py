M = int(input().strip())
n = int(input().strip())

def dfs(m, mul):
    if m == M:
        return n, n
    tmp = mul*m
    last, sum = dfs(m+1, tmp)
    this = last+tmp+1
    sum += this
    print(this, sum)
    return this, sum


print(dfs(1, 1)[1])
