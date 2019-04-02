"""
本题使用的是栈和字典，我用的是从后向前遍历数组，其中字典存的是这个数右边最大的一个数。栈的作用就是在遍历的过程中一直存储着满足条件的大树。
假设在遍历到某个数的时候，从栈顶开始检查，如果栈顶元素大于当前元素，则当前元素右边第一个比它大的数就是栈顶元素；如果比它小，则栈顶元素出栈，
继续判断。到最后如果栈为空时，说明该数的右边没有比它大的，所以按照题意设为-1。不管哪种结果，最后都要将当前的数加入栈。为下一个遍历到的数做
准备。
"""
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        stack = []
        for num in nums2[::-1]:
            while stack:
                if stack[-1] > num:
                    dict[num] = stack[-1]
                    break
                else:
                    stack.pop()
            if not stack:
                dict[num] = -1
            stack.append(num)
        print(dict)
        print(stack)
        return [dict[num] for num in nums1]


solve = Solution()
# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
nums1 = []
nums2 = []
print(solve.nextGreaterElement(nums1, nums2))