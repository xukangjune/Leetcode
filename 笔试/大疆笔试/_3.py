V, N = map(int, input().strip().split(' '))
price = list(map(int, input().strip().split(' ')))
M = int(input().strip())
like = list(map(lambda x: int(x)-1,input().strip().split(' ')))
ret = 0
unlike = [i for i in range(N) if i not in like]



def dfs2(rest, i):
    ret1 = 0
    if i == N-M:
        if rest == 0:
            return 1
        return 0

    if rest == 0:
        return 1

    k = rest // price[unlike[i]]
    for j in range(k+1):
        tmp = dfs2(rest-price[unlike[i]]*j, i+1)
        ret1 += tmp
    return ret1


def dfs(total, i, last):
    global ret

    if total == 0:
        ret += 1
        return

    if i == M:
        ret += dfs2(total, 0)
        return

    k = total // price[like[i]]

    j = min(last-1, k)
    while j >= 1:
        dfs(total-price[like[i]]*j, i+1, j)
        j -= 1

dfs(V, 0, float("inf"))

print(ret)




