T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    nums = list(map(int, input().strip().split(" ")))

    ret = 0
    total = 0
    queue = []
    for num in nums:
        if total <= num:
            total += num
            queue.append(num)
        else:
            ret = max(ret, len(queue))
            while queue and total > num:
                total -= queue.pop(0)
                # print(total)
            total += num
            queue.append(num)
    print(ret)