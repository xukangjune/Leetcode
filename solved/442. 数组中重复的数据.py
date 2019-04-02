"""
这一题很奇妙，题目条件是O(n)的时间复杂度，O(1)的空间复杂度。所以要求在原位上遍历。题目中有一个条件是0<nums[i]>len(nums)，所以数组中的
所有元素都可以用来作为该数组的下标，这一点很重要。所以，数组中重复的元素作为下标指向的是同一个位置，那么就可以对这个位置上的元素进行操作，这
里是将该元素取倒数。所以在遍历时，先取绝对值（因为可能为负），再减一（更加符合数组下标）。如果该数作为下标在数组中的数大于零，说明是第一次遇
到，那么将该数取倒数；如果作为下标对应的数小于零，说明之前已经处理过，那么遍历到的数是第二次出现，加入返回列表中。
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            m = abs(nums[i]) - 1
            if nums[m] > 0:
                nums[m] *= -1
            else:
                ret.append(m+1)
        return ret
solve = Solution()
nums = [4,3,2,7,8,2,3,1]
print(solve.findDuplicates(nums))