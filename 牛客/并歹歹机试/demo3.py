N, K = map(int, input().split(' '))
segments = []
for i in range(N):
    segment = list(map(int, input().split(' ')))
    segments.append(segment)
segments.sort(key=lambda x: (x[0], x[1]))
print(segments, N, K)
if K == 1:
    ret = segments
else:
    ret = []
    count = 0
    prev = None
    for i in segments:
        if not count:
            prev = i
            count += 1
            continue
        else:
            if i[0] > prev[1]:
                prev = i
                count = 0
                continue
            else:
                prev = [i[0], prev[1]]
                count += 1
                if count == K:
                    ret.append(prev)


print(ret)