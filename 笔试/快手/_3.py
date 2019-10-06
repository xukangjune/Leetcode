def func(arr, n):
    nums = sum(arr)
    dp = [[0] * (nums // 2+ 1) for _ in range(n+1)]
    for i in range(n):
        for j in range(1, nums//2+1):
            dp[i+1][j] = dp[i][j]
            if (arr[i] <= j and dp[i][j-arr[i]]+arr[i]>dp[i][j]):
                dp[i+1][j] = dp[i][j-arr[i]]+arr[i]

    return nums-2*dp[n][nums//2]

n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))
print(func(arr, n))