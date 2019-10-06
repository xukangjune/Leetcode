n = int(input().strip())
k = n // 2
dp = [0] * (k+1)
dp[0] = 1

if k == 1:
    print(1)
elif k == 2:
    print(2)
elif k == 3:
    print(5)
else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5
    for i in range(4, k+1):
        for j in range(0, i):
            dp[i] += dp[j] * dp[i-1-j]
    print(dp[k] % 1000000007)

