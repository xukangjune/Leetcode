direction = N = int(input().strip())
grid = []
for i in range(4):
    tmp = list(map(int, input().strip().split(" ")))
    grid.append(tmp)

ret = [[0] * N for i in range(N)]

if direction == 1:
    for i in range(4):
        tmp = [grid[j][i] for j in range(4) if grid[j][i] != 0]
        for j in range(4):
            grid[j][i] = 0

        k = 0
        while k < len(tmp):
            if k+1 < len(tmp) and tmp[k] == tmp[k+1]:
                tmp[k] *= 2
                tmp[k+1] = 0
            k += 1

        n = 0
        for num in tmp:
            if num != 0:
                grid[n][i] = num
                n += 1

if direction == 2:
    for i in range(4):
        tmp = [grid[j][i] for j in range(4) if grid[j][i] != 0]
        for j in range(4):
            grid[j][i] = 0

        k = len(tmp)-1
        while k >= 0:
            if k-1 >= 0 and tmp[k] == tmp[k-1]:
                tmp[k] *= 2
                tmp[k-1] = 0
            k -= 1
        n = 3
        for num in reversed(tmp):
            if num != 0:
                grid[n][i] = num
                n -= 1


if direction == 3:
    for i in range(4):
        tmp = [grid[i][j] for j in range(4) if grid[i][j] != 0]
        for j in range(4):
            grid[i][j] = 0

        k = 0
        while k < len(tmp):
            if k+1 < len(tmp) and tmp[k] == tmp[k+1]:
                tmp[k] *= 2
                tmp[k+1] = 0
            k += 1

        n = 0
        for num in tmp:
            if num != 0:
                grid[i][n] = num
                n += 1

if direction == 4:
    for i in range(4):
        tmp = [grid[i][j] for j in range(4) if grid[i][j] != 0]
        for j in range(4):
            grid[i][j] = 0


        k = len(tmp) - 1
        while k >= 0:
            if k - 1 >= 0 and tmp[k] == tmp[k - 1]:
                tmp[k] *= 2
                tmp[k - 1] = 0
            k -= 1

        n = 3
        for num in reversed(tmp):
            if num != 0:
                grid[i][n] = num
                n -= 1


for i in range(4):
    print(' '.join(map(str, grid[i])))
