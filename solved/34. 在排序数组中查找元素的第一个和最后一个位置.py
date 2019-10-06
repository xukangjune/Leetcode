"""
用的两个二分法，第一二分法是找出最左边的出现的第一个数，用的就是普通的二分法。而第二个就是将原来的二分法做了一些改进，这个二分法可能返回正确的结果，也
可能返回一个不正确的，返回不正确的还要做一次判断。
"""
class Solution:
    def searchRange(self, nums, target):
        ret1, ret2 = -1, -1
        if not nums or nums[-1] < target:
            return [ret1, ret2]

        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target:
                ret1 = left
                break
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] == target:
                right = mid
            else:
                left = mid+1

        left = 0
        right = len(nums) - 1
        while left < right:
            print(left, right)
            if nums[right] == target:
                ret2 = right
                break
            mid = (left + right) // 2 + 1
            print(mid)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid
            else:
                right = mid-1

            print(left, right)
        if nums[left] == target and ret2 == -1:
            ret2 = left

        return [ret1, ret2]


solve = Solution()
# nums = [5,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,10]
target = 6
nums = [5,7,7,8,8,10]
# nums = [1,2,3,3,3,3,4,5,9]
# nums = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
print(solve.searchRange(nums, target))