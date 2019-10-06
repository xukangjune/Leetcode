n, m = map(int, input().split(" "))
grid =[]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(grid, x0, y0, color):
    count = 1
    ret = [[x0, y0]]
    grid[x0][y0] = 0

    while ret != []:
        for item in ret:
            x , y = item[0], item[1]
            tmp = []
            for i, j in directions:
                if 0<=x+i<n and 0<=y+j<n and grid[x+i][y+j] == color and [x+i, y+j] not in ret and [x+i, y+j] not in tmp:
                    tmp.append([x+i, y+j])
                    grid[x+i][y+j] = 0
            ret = tmp
            count += len(ret)

    if count == 1:
        print("only one!")
        grid[x0][y0] = color
        return grid
    else:
        print(count)

    newGrid = [[0] * n for i in range(n)]
    k = 0
    for i in range(n):
        tmp = [grid[j][i] for j in range(n)]
        if tmp.count(0) == n:
            continue
        else:
            p = 0
            for num in tmp:
                if num != 0:
                    newGrid[p][k] = num
                    p += 1
            k += 1
    return newGrid



for i in range(n):
    line = list(map(int, input().strip().split(" ")))
    grid.insert(0, line)

position = []
for q in range(m):
    x0, y0 = map(lambda x: int(x)-1, input().split(" "))
    position.append([x0, y0])

for item in position:
    x0, y0 = item[0], item[1]
    if grid[x0][y0] == 0:
        print("empty!")
        continue
    else:
        grid = bfs(grid, x0, y0, grid[x0][y0])
        print(grid)
    # print(grid)
