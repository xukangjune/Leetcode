n, m = map(int, input().strip().split(" "))
dp = [[0] * m for i in range(n)]


if n==0 or m==0:
    print(0)
else:
    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j] = 1
    print(dp)

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp)
    print(dp[n - 1][m - 1])
