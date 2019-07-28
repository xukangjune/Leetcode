"""
我的解法先是用遍历的手段，将首尾相同的数字，去掉一个（去掉尾部，或首部）。还有一点，那就是第一次去掉首尾相同的数字后，中间就不会出现首尾相同的
数字了，所以一劳永逸。
"""
class Solution:
    def findMin(self, nums) -> int:
        # 这是另一种写法，我感觉还是O(n)的时间复杂度啊
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                l = m
            else:
                r -= 1
        return nums[l]


        # 这是自己写的，复杂度编程了O(n)
        # n = len(nums)
        # if n < 2:
        #     return nums[0]
        # l = 0
        # r = n-1
        # while l < r:
        #     if nums[l] == nums[r]:
        #         l += 1
        #     else:
        #         break
        #
        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m
        # return nums[l]


solve = Solution()
nums = [2,2,2,0,1]
# nums = [1,3,5]
# nums = [2,2,2,0,1,1,2,2]
# nums = [2,2,2,2,2,2,2,2]
# nums = [1,2,1]
print(solve.findMin(nums))