T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    nums = list(map(int, input().strip().split(" ")))

    total = sum(nums)
    if total % 2:
        print("NO")
    elif n == 2:
        if nums[0] == nums[1]:
            print("YES")
        else:
            print("NO")
    else:
        half = total // 2
        queue = [nums[0]]
        tmp = nums[0]
        j = 1
        while tmp != half and j < n:
            if tmp + nums[j] > half:
                while queue and tmp + nums[j] > half:
                    tmp -= queue.pop(0)
            tmp += nums[j]
            queue.append(nums[j])
            j += 1

        if tmp == half:
            print("YES")
        else:
            print("NO")

