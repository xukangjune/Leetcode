#不会
N = int(input().strip())
w = sorted(list(map(int, input().strip().split(" "))), reverse=True)



ret = N-2
all = sum(w)
rest = all - 2*w[0]
if rest <= 0:
    print(abs(rest), N)
else:
    for i in range(1, N):
        pass








total = w[0]


for i in range(1, N):
    tmp = total + w[i]
    if abs(all-2*total) <= abs(all-2*tmp):
        break
    total = tmp
    ret -= 2

print(abs(all - 2*total), ret)

