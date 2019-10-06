N = int(input().strip())
pos = list(map(int, input().strip().split(',')))

dp = [0] * N
temp = 0
ret = float("inf")
for i in range(1,N):
    dp[i] = abs(pos[i] - pos[i-1]) + dp[i-1]
for i in range(1, N-1):
    ret = min(ret, dp[N-1]-abs(pos[i]-pos[i-1])-abs(pos[i+1]-pos[i])+abs(pos[i+1]-pos[i-1]))
print(ret)