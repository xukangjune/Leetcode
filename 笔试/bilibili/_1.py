word1 = input().strip()
word2 = input().strip()

n = len(word1)
m = len(word2)

if n *m == 0:
    print(n+m)
else:
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if (i==0):
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif(word1[i-1] == word2[j-1]):
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1

    print(dp[n][m])