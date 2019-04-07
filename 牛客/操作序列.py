n = int(input())
# nums = list(map(int, input().split()))
# ret = []
# odd = [nums[i] for i in range(n) if i % 2 ]
# even = [nums[i] for i in range(n) if i % 2 ==0]
# print(odd)
# print(even)
# if n % 2:
#     print(' '.join(map(str, even[::-1])) + ' ' + ' '.join(map(str, odd)))
# else:
#     print(' '.join(map(str, odd[::-1])) + ' ' + ' '.join(map(str, even)))

nums = ''.join(input().split(" "))
print(nums[-1::-2])
print(nums[::2])
print(' '.join(nums[-1::-2]) + ' ' + ' '.join(nums[n%2::2]))