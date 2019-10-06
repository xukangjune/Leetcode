n = int(input().strip())
nums = sorted(list(map(int, input().strip().split(" "))))
if n == 0:
    print()
else:
    if n % 2:
        print(nums[n//2])
    else:
        print(nums[n//2-1])