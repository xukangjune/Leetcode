n, m, k = map(int, input().strip().split(" "))
grid = [[0] * m for i in range(n)]
for i in range(k):
    x, y = map(int, input().strip().split(" "))
    if x == 0 and y == 0:
        print(0)
        break
    elif x == n-1 and y == m-1:
        print(0)
        break
    grid[x][y] = 1

else:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ret = float("inf")

    def dfs(x, y, count):
        global ret
        if x == n - 1 and y == m - 1:
            ret = min(count, ret)
            return
        grid[x][y] = 1
        for d in directions:
            i, j = d
            if x + i < 0 or x + i >= n or y + j < 0 or y + j >= m or grid[x + i][y + j] != 0:
                continue
            dfs(x + i, y + j, count + 1)
        grid[x][y] = 0
        return

    dfs(0, 0, 0)
    if ret == float("inf"):
        print(0)
    else:
        print(ret)