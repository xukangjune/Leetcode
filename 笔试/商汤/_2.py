n = int(input().strip())
nums = list(map(int, input().strip().split(" ")))

ret = float("-inf")
for i in range(n):
    count = nums[i]
    j = i+1
    if count < 0:
        count = 0
    while j > i and j%n!=i:
        tmp = j%n
        count += nums[tmp]
        if count > ret:
            ret = count
        if count < 0:
            count = 0
        j += 1

print(ret)