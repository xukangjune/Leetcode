T = int(input().strip())
for _ in range(T):
    nums = list(map(int, input().strip().split(" ")))
    a = min(nums)
    b = sorted([num-a for num in nums if num > a])
    ret = a

    if len(b) == 2:
        if 2 * b[0] <= b[1]:
            ret += b[0]
            c = b[1] - 2*b[0]
            if c % 2:
                ret += (c // 2 + 1)
            else:
                ret += c // 2
        else:
            ret += b[0]
            c = b[1] - b[0]



    elif len(b) == 1:
        ret += (b[0]//2+1)
        c = b[0]
        if c % 2:
            ret += (c // 2 + 1)
        else:
            ret += c // 2
        print(ret)
    else:
        print(ret)





