"""
本题要使用O(1)空间复杂度的原地算法，所以不能出现数组复制等操作。可以先将数组分成两部分，分别是0~n-k-1和n-k~n-1。这两部分可以先做旋转，
即首尾的元素全部颠倒。其实Python数组的有个方法可以直接实现颠倒，但是若将部分颠倒，则要先复制这样就违背了空间复杂度的要求。所以自己写了
个辅助函数。最后将整个数组进行颠倒，可以直接使用reverse方法。
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
         """
        n = len(nums)
        k %= n
        self.exchange(0, n-k-1)
        self.exchange(n-k, n-1)
        nums.reverse()

    def exchange(self, first, last):
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1

solve = Solution()
nums = [1,2,3,4,5,6]
solve.rotate(nums, 11)
print(nums)
