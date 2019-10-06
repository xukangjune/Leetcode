# M, N = map(int, input().split(' '))
# buildings = list(map(int, input().split(' ')))
# heights = {}
# for building in buildings:
#     if building not in heights:
#         heights[building] = 0
#     heights[building] += 1
#
# print(heights)
#
# buildingsNumsSoFar = 0
#
# ret = float("inf")
# keys = sorted(heights.keys())
# for i, key in enumerate(keys):
#     if heights[key] >= N:
#         ret = 0
#         break
#
#     diff =  N - heights[key]
#     if buildingsNumsSoFar < diff:
#         buildingsNumsSoFar += heights[key]
#         continue
#
#     tempSum = 0
#     currHeight = key
#
#     j = i - 1
#     while j >= 0 and diff > 0:
#         if diff >= heights[keys[j]]:
#             tempSum += (currHeight - keys[j]) * heights[keys[j]]
#         else:
#             tempSum += (currHeight - keys[j]) * diff
#         diff -= heights[keys[j]]
#     ret = min(ret, tempSum)
#
# print(ret)


M, N = map(int, input().split(' '))
buildings = list(map(int, input().split(' ')))
buildings.sort()
dp = [float("inf")] * M
dp[N-1] = buildings[N-1] * N - sum(buildings[:N])
for i in range(N, M):
    dp[i] = (buildings[i] - buildings[i-1]) * N + dp[i-1] - (buildings[i] - buildings[i-N])
print(dp)
print(min(dp))