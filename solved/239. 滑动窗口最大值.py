"""
终于通过了。开始我用的是堆排序，上浮下沉什么的，很繁琐，而且还是用C++写的。后来看来解答，豁然开朗，具体的分析可以看这里：
https://blog.csdn.net/fulongxu/article/details/80978243
"""
class Solution:
    def maxSlidingWindow(self, nums, k):
        queue = []
        ret = []
        for i in range(len(nums)):
            if not queue or nums[i] > nums[queue[-1]]:
                while queue and nums[i] > nums[queue[-1]]:
                    queue.pop()
                queue.append(i)
            elif nums[i] <= nums[queue[-1]]:
                queue.append(i)
            if i >= k-1:
                if i - queue[0] >= k-1:
                    ret.append(nums[queue.pop(0)])
                else:
                    ret.append(nums[queue[0]])
        return ret


solve = Solution()
nums = [1,-9,8,-6,6,4,0,5]
print(solve.maxSlidingWindow(nums, 4))