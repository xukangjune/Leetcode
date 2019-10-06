n = int(input().strip())
times = {}
count = 0

for _n in range(n):
    i, j = map(int, input().strip().split(" "))
    times[j] = i
    count += i
time_sort = sorted(times.keys())
# print(times)
# print(time_sort)
# print(count)

l = 0
r = len(time_sort)-1
# print(l ,r)
ret = time_sort[l]+time_sort[r]

while count > 0 and time_sort[l] != time_sort[r]:
    ret = max(ret, time_sort[l]+time_sort[r])
    if times[time_sort[l]] > times[time_sort[r]]:
        times[time_sort[l]] -= times[time_sort[r]]
        r -= 1
    elif times[time_sort[l]] < times[time_sort[r]]:
        times[time_sort[r]] -= times[time_sort[l]]
        l += 1
    else:
        l += 1
        r -= 1
    count -= 2


print(ret)