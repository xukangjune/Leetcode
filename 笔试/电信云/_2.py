n = int(input().strip())
ret = ''

ret += n // 1000 * 'M'
n %= 1000
ret += n // 500 * 'D'
n %= 500
ret += n // 100 * 'C'
n %= 100
ret += n // 50 * 'L'
n %= 50
ret += n // 10 * 'X'
n %= 10
ret += n // 5 * 'V'
n %= 5
ret += n // 1 * 'I'

print(ret)