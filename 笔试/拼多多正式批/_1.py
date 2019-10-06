n, m = map(int, input().strip().split(" "))
nums = list(map(int, input().strip().split(" ")))

nums.sort()
a = nums[:m*2]
ret = 0
l = 0
r = 2*m-1
while l < r:
    ret += nums[l] * nums[r]
    l += 1
    r -= 1
print(ret)
