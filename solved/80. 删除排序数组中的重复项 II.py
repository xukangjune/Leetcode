"""
这里第二种解答是我自己写的，用了双指针，第一个指针指向的是第一个不满足需要的位置（也是最后返回的值），第二个指针一直向后
遍历，它是最后终止的条件。这里用一个count来记录前面同一数出现的次数。
第一种解法是我看的别人写的，十分巧妙。它用到了2这个数字。因为原数组是排序的，而且要求返回的数组最多有两个相同的数字。所以
在i>=2时，返回数组中一定右nums[i]>nums[i-2]。在i<2时，可以直接将原数组不用改变。从数组的第三个数开始，如果这个数大于
nums[i-2],说明这个数可以放在nums[i]（此时前面没有重复），如果等于nums[i-2]，这说明前面已经出现过了，不满足，继续遍历
数组，i不动。
"""
class Solution:
    def removeDuplicates(self, nums):
        # 高手
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i

        # 中规中矩，比较笨
        # if nums:
        #     count = 1
        #     prev = nums[0]
        #     left = right = 1
        #     while right < len(nums):
        #         if nums[right] != prev:
        #             prev = nums[right]
        #             if left < right:
        #                 nums[left], nums[right] = nums[right], nums[left]
        #             count = 1
        #             left += 1
        #         elif nums[right] == prev:
        #             if count < 2:
        #                 if left < right:
        #                     nums[left], nums[right] = nums[right], nums[left]
        #                 count += 1
        #                 left += 1
        #         right += 1
        #     print(nums)
        #     return left


solve = Solution()
nums = [1,1,1,2,2,3]
print(solve.removeDuplicates(nums))
