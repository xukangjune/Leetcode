"""开始自己写的很慢，原因是在while循环中使用了大量的min()函数。
后来看到网上的解法，学习了新的知识。就是在while循环中先不用min函数，而是先不断的将最左边
的数减去，如果大于s就停止。这样减到最后，就获得了一个最小长的的满足题意得子序列，为i-left+2。
与之前得比较，就可以获得最短的序列。
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        if not (nums and s):
            return 0
        temp = 0
        ret = float("inf")
        left = 0
        for i, num in enumerate(nums):
            if num >= s:
                return 1
            if temp < s:
                temp += num
            if temp >= s:
                while temp >= s:
                    temp -= nums[left]
                    left += 1
                ret = min(ret, i-left+2)
        return 0 if ret == float('inf') else ret


solve = Solution()
# s = 7
# nums = [2,3,1,4,3]
s=3
nums=[1,1]
print(solve.minSubArrayLen(s, nums))