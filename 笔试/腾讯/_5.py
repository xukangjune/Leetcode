from collections import defaultdict
n = int(input().strip())
a_map = defaultdict(int)
b_map = defaultdict(int)
a_set = set()
b_set = set()
# sum_map = defaultdict(int)

for num in map(int, input().strip().split(" ")):
    a_map[num] += 1
for num in map(int, input().strip().split(" ")):
    b_map[num] += 1
# print(a_map)
# print(b_map)

ret = 0
for a in a_map.keys():
    for b in b_map.keys():
        tmp = a_map[a] * b_map[b]
        if tmp % 2:
            ret ^= (a+b)
print(ret)