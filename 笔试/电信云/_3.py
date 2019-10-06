nums = eval(input().strip())
ret = float("-inf")

tmp = 0
for num in nums:
    tmp += num
    if tmp > ret:
        ret = tmp
    if tmp < 0:
        tmp = 0

print(ret)