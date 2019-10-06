from collections import defaultdict

map = defaultdict(int)
ret = 0
n = int(input().strip())
xi = list(input().strip().split(' '))
for num in xi:
    map[num] += 1

keys = sorted(map.keys(), reverse=True)

for key in keys:
    if map[key] > 1:
        pass


print(map)
print(keys)

