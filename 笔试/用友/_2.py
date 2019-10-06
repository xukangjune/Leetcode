# line = int()
# deli = line.index(',')

# P = int(line[4:deli])
# V = eval(line[deli+3:])
P = int(input().strip())
V = list(map(int, input().strip().split(" ")))
V.sort()

print(P)
print(V)

if P == 0 or V == [] or P < V[0]:
    print(0)
else:
    ret = 0
    l = 0
    r = len(V)-1
    while l <= r:
        if P >= V[l]:
            P -= V[l]
            l += 1
            ret += 1
        elif ret > 0:
            if r > l:
                ret -= 1
                P += V[r]
                r -= 1
            else:
                break
        else:
            break

    print(ret)

print(P)
print(V)