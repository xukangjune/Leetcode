from math import sqrt
from collections import defaultdict

n = int(input().strip())
candies = list(map(int, input().strip().split(" ")))

nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]
for i in range(24, 20000):
    for j in range(2, int(sqrt(i))):
        if i % j == 0:
            break
    else:
        nums.append(i)

map = defaultdict(int)
for num in nums:
    map[num] = [num, 1]

def find_parent(i):
    if tmp[i] != i:
        return find_parent(tmp[i])
    return i

tmp = nums[:]


for candy in candies:
    for i in nums:
        pass
