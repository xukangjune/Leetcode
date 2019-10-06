n, m, k = map(int, input().strip().split(" "))

cnt = 0
def dfs(word, a, b):
    global cnt
    ret = False
    if cnt == k:
        print(word)
        return True
    elif a == n and b == m:
        return False
    if a < n:
        cnt += 1
        ret = dfs(word+'a', a+1, b)
    if not ret and b < m:
        cnt += 1
        ret = dfs(word+'b', a, b+1)
    return ret

dfs('', 0, 0)
