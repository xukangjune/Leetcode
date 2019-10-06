S = int(input().strip())
for i in range(S):
    ret = []
    m = input().strip()
    b = input().strip()
    for c in b:
        if c not in m:
            print("{")
            print("}")
            break

    else:
        k = 0
        p = 0
        ret = ''
        while k < len(m):
            if m[k] in b:
                p = b.index(m[k])
                break
            k += 1

        for _k in range(k):
            ret += 'd'
        ret = [ret + 'l', ret + 'r']

        pos = [[p, p, '']]
        for idx in range(k + 1, len(m)):
            c = m[idx]
            tmpPos = []
            for _pos in pos:
                l = _pos[0]
                r = _pos[1]
                lr = _pos[2]

                if (l - 1 >= 0 and b[l - 1] != c) and (r + 1 < len(b) and b[r + 1] != c):
                    tmpPos.append([l, r, lr + 'd'])
                    continue

                if l - 1 >= 0 and b[l - 1] == c:
                    tmpPos.append([l - 1, r, lr + 'l'])
                if r + 1 < len(b) and b[r + 1] == c:
                    tmpPos.append([l, r + 1, lr + 'l'])

            pos = tmpPos

        if pos:
            ans = []
            for po in pos:
                for re in ret:
                    ans.append(re + po[2])
                    ret = ans

        print('{')
        for re in ret:
            print(' '.join(re))
        print('}')

