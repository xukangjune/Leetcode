from collections import defaultdict

k = int(input().strip())
s = input().strip()
map = defaultdict(int)
n = 0
char = []
ret = 0
start = 0

if k == 0:
    print(0)

else:
    for i, c in enumerate(s):
        if c not in map:
            if n == k:
                ret = max(ret, i - start)
                start = map[char[0]] + 1
                del map[char[0]]
                char.pop(0)

            else:
                n += 1

            char.append(c)
            map[c] = i

        else:
            map[c] = i

    ret = max(ret, len(s) - start)

    print(ret)
print(map)





