"""
本题先判断原数组与排序过的数组是否相同，如果相同，说明不需要移动元素，返回0。如果不同，就分别从两个方向开始遍历，出现不相同的元素就返回索引，
然后直接将索引相减。
看了其它解法，大同小异。
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortNum = sorted(nums)
        if nums == sortNum:
            return 0
        length = len(nums)
        first = 0
        last = length - 1
        for i in range(length):
            if nums[i] != sortNum[i]:
                first = i
                break
        for j in range(length-1, -1, -1):
            if nums[j] != sortNum[j]:
                last = j
                break
        return last - first + 1




solve = Solution()
# nums = [1,1,2]
nums = [1,2,1]
# nums = [2, 6, 4, 8, 10, 9, 15]
# nums = [5,4,3,2,2,1]
# nums = [3]
# nums = [2,3,3,2,4]
print(solve.findUnsortedSubarray(nums))