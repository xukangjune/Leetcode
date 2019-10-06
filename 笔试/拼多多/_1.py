nums, N = input().strip().split(';')
nums = list(map(int, nums.split(',')))
N = int(N)


odds = []
even = []
for num in nums:
    if num % 2:
        odds.append(num)
    else:
        even.append(num)

odds.sort(reverse=True)
even.sort(reverse=True)

if N <= len(even):
    print(','.join(map(str, even[:N])))
else:
    even.extend(odds[:N - len(even)])
    print(','.join(map(str, even)))
