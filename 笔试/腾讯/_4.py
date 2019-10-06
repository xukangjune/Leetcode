n, k = map(int, input().strip().split(" "))
nums = list(map(int, input().strip().split(" ")))
nums.sort()

count = 0
prev = 0

for idx, num in enumerate(nums):
    if num-prev <= 0:
        continue
    else:
        print(num-prev)
        prev = num
        count += 1
        if count == k:
            break

while count < k:
    print(0)
    count += 1



