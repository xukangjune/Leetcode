T = int(input().strip())
for _ in range(T):
    n = int(input().strip())

    if (n//10==0):
        print(n)
    else:
        ret = 9
        tmp = 9
        while n>tmp:
            if (n-tmp)>=9:
                ret = ret*10+9
                tmp += 9
            else:
                diff = n-tmp
                ret = int(str(diff)+str(ret))
                tmp = n
        print(ret)