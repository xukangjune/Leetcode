N, K = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
ret = nums[0] + nums[1] - N
for num in nums[2:]:
    if ret <= 0:
        break
    ret = ret + num - N
print(ret if ret >= 0 else 0)
