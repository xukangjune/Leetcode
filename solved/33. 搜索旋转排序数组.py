"""
这道题想了好久都没做出来。我之前的想法是利用二分法寻找的过程中，判断中间值和目标值是在递增位置上，还是横跨旋转值，到那时这样想了好久都没有想通这个边界
问题（我非常讨厌这个）。后来看到有人分两步做的，先找到旋转的位置（可得到旋转的长度），然后在原数组中进行二分法时，每次将中间值加上这个长度，就是真正的
值，根据这个值与目标值的大小关系，来确定下一步二分法的边界。
试了一下，边界问题有点懂了。我之前用的是target与nums[l]比较的，不好。
"""
class Solution:
    def search(self, nums, target):  
        if not nums:
            return -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


        # 这是使用了两次的二分法
        # if not nums:
        #     return -1
        # n = len(nums)
        # l, r = 0, n-1
        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m
        #
        # ro = l
        # print(ro)
        # l, r = 0, n-1
        # while l <= r:
        #     m = (l + r) // 2
        #     mid = (m + ro) % n
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = m  + 1
        #     else:
        #         r = m - 1
        # return -1


solve = Solution()
# nums = [4,5,6,7,0,1,2,3]
target = 5
# nums = [4,5,6,7,8,1,2,3]
nums = [5,1,3]
print(solve.search(nums, target))