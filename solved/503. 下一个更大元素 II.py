"""
竟然超过了100%，很意外。这一题与上一题有些不同，首先允许了重复元素的出现，所以就不能用字典了，用字典的话会覆盖之前的值。于是我直接在原数组上
操作的，反正当前的值遍历完后，后面就用不到了。另外，这个数组是个循环数组，即首尾是相通的，这就和之前不同了。于是我用的是从最大值的位置开始遍
历。因为最大值的对应的是一定是-1。然后从最大值位置的左边一直遍历到右边（用range实现）。有了这两点，其余的就和第一题一样了。
"""
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        pos = nums.index(max(nums))
        stack = []
        for i in range(pos, pos-len(nums), -1):
            temp = nums[i]
            while stack:
                if stack[-1] > nums[i]:
                    nums[i] = stack[-1]
                    break
                else:
                    stack.pop()
            if not stack:
                nums[i] = -1
            stack.append(temp)
        return nums


solve = Solution()
nums = [100,1,11,1,120,111,123,1,-1,-100]
print(solve.nextGreaterElements(nums))
