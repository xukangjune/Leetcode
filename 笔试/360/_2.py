from collections import defaultdict
s = input().strip()
ret = 0
map = defaultdict(int)
for c in s:
    map[c] += 1
print(max(map.values()))