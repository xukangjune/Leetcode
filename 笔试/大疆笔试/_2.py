while 1:
    line = input().strip().split(' ')
    N, M = int(line[0]), int(line[1])
    print(N, M)
    map = dict()
    for i in range(N+M):
        if i < N:
            cmd, action = input().strip().split(' ')
            map[cmd] = action
        if N <= i < N+M:
            cmd = input().strip()
            print(map[cmd])
