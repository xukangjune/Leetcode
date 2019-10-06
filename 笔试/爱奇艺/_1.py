x, y, z, k = map(int, input().strip().split(" "))

if k == 0:
    print(1)
else:
    o = p = q = 1
    while 1:
        if k == 0:
            print(o*p*q)
            break
        s3 = o * p
        s1 = p * q
        s2 = o * q
        if s1 == s2 == s3:
            if x > 1:
                o += 1
                x -= 1
            elif p > 1:
                p += 1
                y -= 1
            elif q > 1:
                q += 1
                z -= 1
            else:
                print(o * p * q)
                break

        elif s1 > s2 and s1 > s3:
            if x > 1:
                o += 1
                x -= 1
            elif s2 >= s3 and y > 1:
                p += 1
                y -= 1
            elif z > 1:
                q += 1
                z -= 1
            else:
                print(o * p * q)
                break

        elif s2 > s3 and s2 > s1:
            if y > 1:
                p += 1
                y -= 1
            elif s1 >= s3 and x > 1:
                o += 1
                x -= 1
            elif z > 1:
                q += 1
                z -= 1
            else:
                print(o * p * q)
                break

        else:
            if z > 1:
                q += 1
                z -= 1
            elif s2 >= s1 and y > 1:
                p += 1
                y -= 1
            elif x > 1:
                o += 1
                x -= 1
            else:
                print(o * p * q)
                break

        k -= 1



