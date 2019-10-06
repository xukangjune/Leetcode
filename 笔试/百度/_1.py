a, b, n = map(int, input().strip().split(" "))

tmp = a*b
carry = tmp // 10
ans = a*b % 10
count = ans * n
count += carry * n
print(count)
