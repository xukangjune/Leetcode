from collections import defaultdict
N = int(input())
map_x = defaultdict(list)
map_y = defaultdict(list)

for i in range(N):
    x, y = map(int, input().strip().split(" "))
    map_x[x].append(y)
    map_y[y].append(x)

nx = sorted(map_x.keys())
my = sorted(map_y.keys())


vertical = [0] * 10000
level = [0] * 10000


