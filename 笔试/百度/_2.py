n, m = map(int, input().strip().split(" "))
grid = []
for _ in range(n):
    line = input().strip()
    tmp = []
    for c in line:
        tmp.append(c)
    grid.append(tmp)
x, y = map(lambda x:int(x)-1, input().strip().split(" "))

# print(grid)
# print(x, y)

count = 0
move = [0, 0]
map = {'N':[-1, 0], 'S':[1, 0], 'E':[0, 1], 'W':[0, -1]}
while 0<=x<n and 0<=y<m:
    if grid[x][y] == 'N':
        move = map['N']
    elif grid[x][y] == 'S':
        move = map['S']
    elif grid[x][y] == 'E':
        move = map['E']
    elif grid[x][y] == 'W':
        move = map['W']

    grid[x][y] = ''
    x += move[0]
    y += move[1]
    count += 1
print(count)