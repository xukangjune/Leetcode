N = int(input().strip())
nums = list(map(int, input().strip().split(" ")))

zeros = 0
ones = 0
i = 1
if nums[0] == 0:
    zeros = 1
else:
    ones = 1

segments = []

while i < N-1:
    if nums[i] == 1:
        while i+1 < N-1 and nums[i+1] == 1:
            i += 1
        if i+1 < N-1:
            segments.append(i+1)
        zeros += 1
        i += 1
    if nums[i] == 0:
        while i+1 < N-1 and nums[i+1] == 0:
            i += 1
        if i+1 < N-1:
            segments.append(i+1)
        ones += 1
        i += 1


ret = 1
tmp = []
prev = 0
for num in nums:
    tmp.append(num-prev)
