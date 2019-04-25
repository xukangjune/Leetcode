ret = [0] * (10000001)
for i in range(2, 10001):
    j = i
    while i*j < 10000000:
        ret[i*j] = 1
        j += 1

for i in range(10000000, 1, -1):
    if not ret[i]:
        temp = ret[i]
        bag = set()
        while temp:
            last = temp % 10
            if last in bag:
                break
            else:
                bag.add(last)
                temp //= 10
        if temp == 0:
            print(ret[i])
