n = int(input().strip())
count = 0

while n:
    count += 1
    n &= (n-1)

print(count)