"""
没有什么特别的，就是遍历一遍数组，然后查找断点处。带我复习了一下格式化字符串
"""
class Solution:
    def summaryRanges(self, nums):
        ret = []
        if nums:
            current = nums[0]
            prev = current
            for num in nums[1:]:
                if num == current+1:
                    current = num
                else:
                    if prev == current:
                        ret.append('%d' %prev)
                    else:
                        ret.append('%d->%d' %(prev, current))
                    prev = current = num
            if prev == current:
                ret.append('%d' % prev)
            else:
                ret.append('%d->%d' % (prev, current))
        return ret


solve = Solution()
nums = [1,2,4,5,6,8]
print(solve.summaryRanges(nums))