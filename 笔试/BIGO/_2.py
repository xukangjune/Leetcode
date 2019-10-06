def func(nums):
    n = len(nums)
    dp = [[0] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = nums[i]

    for i in range(n):
        for j in range(i+1, n):
            dp[i][j] = dp[i][j-1] + dp[j][j]

    print(dp)

    v = [[dp[i][j] for i in range(n)] for j in range(n)]
    maxes = []
    for op in v:
        maxes.append(max(op))
    print(maxes)



nums = [-1, 2, 5, 7, -3, 1, -5, 2, 8, 9, 1, -11, -12, 13, 2, 5]
func(nums)
