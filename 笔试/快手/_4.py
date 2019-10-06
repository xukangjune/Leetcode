n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))
arr.sort()

if n == 0:
    print(0)
else:
    ret = 0
    dp = [{} for _ in range(n)]
    for i in range(n):
        for j in range(i):
            tmp = arr[i]-arr[j]
            k = dp[j].get(tmp, 1)+1
            dp[i][tmp] = k
            ret = max(ret, dp[i][tmp])
    print(ret)
