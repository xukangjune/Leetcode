"""
看的解答写出来的，总的时间复杂度为平方级别的。首先将nums排序，然后将第一个值从0遍历到n-2。每次遍历时，第二个值为第一个值位置加1，第三个值为最后一个
位置，每次将三个数相加，如果等于target那么就可以直接输出，如果大于target，那么third减1，否则second加1，注意在这个过程中，可以跳过重复项。
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int 
        :rtype: int
        """
        n = len(nums) - 1
        nums.sort()
        first, second, third = 0, 1, n
        ret = nums[first] + nums[second] + nums[third]
        for first in range(n-1):
            if first > 0 and nums[first] == nums[first-1]: #消除重复项
                continue
            second = first + 1
            third = n
            while second < third:
                temp = nums[first] + nums[second] + nums[third]
                if temp == target:
                    return temp
                if temp > target:
                    third -= 1
                    while second < third and nums[third] == nums[third+1]: #消除重复项
                        third -= 1
                elif temp < target:
                    second += 1
                    while second < third and nums[second] == nums[second-1]: #消除重复项
                        second += 1
                if abs(temp-target) < abs(ret-target):
                    ret = temp
        return ret

solve = Solution()
nums = [-1,2,1,-4]
target = 1
# nums = [0,0,0]
# target = 1
# nums = [1,1,1,0]
# target = 100
# nums = [0,1,2]
# target = 0
# nums = [1,-3,3,5,4,1]
# target = 1
# nums = [4,0,5,-5,3,3,0,-4,-5]
# target = -2
# nums = [1,2,4,8,16,32,64,128]
# target = 82
# nums = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
# target = 0
print(solve.threeSumClosest(nums, target))