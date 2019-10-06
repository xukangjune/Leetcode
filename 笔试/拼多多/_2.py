def dfs(idx, m, n, str, b, op):
    if idx == n:
        if str == b:
            return [op]
        return None

    c = m[idx]
    ans = []
    ret = dfs(idx+1, m, n, str, b, op+'d')
    if ret:
        ans.extend(ret)

    ret = dfs(idx+1, m, n, c+str, b, op+'l')
    if ret:
        ans.extend(ret)


    ret = dfs(idx+1, m, n, str+c, b, op+'r')
    if ret:
        ans.extend(ret)

    return ans


S = int(input().strip())
for i in range(S):
    ret = []
    m = input().strip()
    b = input().strip()
    ans = dfs(0, m, len(m), '', b, '')
    print(ans)

