"""
找质数的的经典算法，埃氏筛法。空间复杂度为n，时间复杂度为nloglogn。
先建立一个长度为n的数组，初始化为True。然后先将i=2，i每次递增1，当isPrime[i]为False时，不必处理，并使得i*i<n。内部的遍历，先使得j= i*i，
并且j+=i，然后保证j<n，让所有的j下标的数组变为False（不是质数）。最后统计的就是从下标2开始到n-1，所有为True的个数。
"""
class Solution:
    def countPrimes(self, n):
        isPrime = [True] * n
        i = 2
        while i * i < n:
            if not isPrime[i]:
                i += 1
                continue
            j = i * i
            while j < n:
                isPrime[j] = False
                j += i
            i += 1
        count = 0
        for flag in isPrime[2:]:
            if flag:
                count += 1
        return count


solve = Solution()
print(solve.countPrimes(1000))