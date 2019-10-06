t = int(input().strip())
for _t in range(t):
    n = int(input().strip())
    s = input().strip()
    if n<11:
        print("NO")
    else:
        idx = n
        if '8' in s:
            idx = s.index('8')
        if n-(idx+1)>=10:
            print("YES")
        else:
            print("NO")