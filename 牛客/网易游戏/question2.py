from sys import stdin
ret = []
while True:
    line = input()
    print(line)
    if line:
        ret.append([int(num) for num in line.split('.')])
    else:
        break
ret.sort(key=lambda x:(x[0], x[1], x[2], x[3]))

for i in ret:
    print('.'.join(map(str, i)))



"""
101.228.198.165
101.24.129.93
10.170.0.17
101.71.253.154
"""