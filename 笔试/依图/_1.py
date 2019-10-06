n = int(input().strip())
nums = list(map(int, input().strip().split(" ")))

i = 0
m = 0
ret = 0
while i < n:
    if nums[i] == 0:
        m += 1
    else:
        if m > 0:
            ret += m // 2
        m = -1
    i += 1
ret += (m+1) //2

print(ret)

