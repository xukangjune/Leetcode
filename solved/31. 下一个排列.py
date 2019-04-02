"""
题目要求原位操作，所以我写了一个交换函数。首先要找到下一个字典序，可以先从后先前遍历，如果发现前面的数小于后面的数，就将这个
数与后面小于大于它最小的数交换位置，然后原来前面数就改变了。而且它后面的数是一个递增的序列，使用辅助函数就可以将递增改为递减
了。这个就是最小的。
如果整个数组都是递减的（说明这是这些数组所能组成的最大的数），那么就需要将整个数组倒序（题目规定的），还是使用辅助函数即可完成。
"""
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        temp = n

        def reverse(first, last):
            while first <= last:
                nums[first], nums[last] = nums[last], nums[first]
                first += 1
                last -= 1

        for i in range(n, -1, -1):
            if nums[i] < nums[temp]:
                while temp <= n and nums[temp] > nums[i]:
                    temp += 1
                nums[i], nums[temp-1] = nums[temp-1], nums[i]
                reverse(i+1, n)
                break
            temp = i
        if temp == 0:
            reverse(0, n)


solve = Solution()
nums = [1,2,3,4,10,13,12,11,8,7,6,5,4,3,2,1]
solve.nextPermutation(nums)
print(nums)
