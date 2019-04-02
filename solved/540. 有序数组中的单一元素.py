"""
这一题要求是在O（log n）的时间复杂度， O（1）的空间复杂度下完成。所以就不能用异或来遍历数组了。使用的是二分法，先设定头位置为0， 尾位置为最
后一个位置，当前位置为中间位置根据下面的情况进行头尾的转换。如果当前位置是偶数，那么当前位置之前的元素总共有奇数个（因为下标从零开始），所以
如果前面的元素都是两两出现的（即要求的数在当前位置后面），那么当前位置的值一定与后一个位置的值相等：如果后面的数是两两出现的，那么当前位置的数
一定和前一个位置的数相等；如果这两种情况都不存在，那么说明当前值就是要返回的值。另外一种情况就是当前值为偶数时，此种情况和前一种正好相反。
另外，在赋值给mid的时候，有一点注意的是，就是mid的值在两种情况下是不一样的。
"""
class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        while first < last:
            mid = (last + first) // 2
            print(first, mid, last)
            if mid % 2:
                if nums[mid] == nums[mid-1]:
                    first = mid + 1
                elif nums[mid] == nums[mid+1]:
                    last = mid - 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid-1]:
                    last = mid - 2
                elif nums[mid] == nums[mid+1]:
                    first = mid + 2
                else:
                    return nums[mid]
        return nums[last]


solve = Solution()
# nums = [1,1,2,3,3,4,4,8,8]
# nums = [3,3,7,7,10,11,11]
nums = [1]
print(solve.singleNonDuplicate(nums))