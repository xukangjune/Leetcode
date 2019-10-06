case = int(input().strip())
for i in range(case):
    N, X = map(int, input().strip().split(' '))
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().strip().split(' '))
    dp = [0] * (X+1)

    for i in range(N):
        next_dp = [0] * (X+1)
        for j in range(B[i], X+1):
            next_dp[j] = max(dp[j], dp[j-B[i]]+A[i])
        dp = next_dp
    print(dp[N][X])

