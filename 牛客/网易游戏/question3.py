from sys import stdin
a = 0
b = 0
while True:
    line = stdin.readline().strip().split()
    if line:
        for i in line:
            k = i.find("=")
            if i[0] == 'a':
                a += int(i[k+1:])
            elif i[0] == 'b':
                b += int(i[k+1:])
    else:
        print("a: %d" % a)
        print("b: %d" % b)
        break


"""
a1=1 a2=2
b3=3 b4=4
a5=5 a6=6
b7=7 b8=8
a9=9 a10=10
"""