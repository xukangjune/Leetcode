"""
线性的时间复杂度。该题的核心就是去除递增和递减序列，只取其中一个数。然而怎么取是有讲究的。首先在递增这一块一定要去最大的，递减取最小的，这样才能保证取到
最大。另外，我用的flag来标志下一次应该是递增还是递减。
"""
class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        currNum = nums[0]
        flag = None
        ret = 1
        for num in nums[1:]:
            if flag is None and num != currNum:
                flag = True if num - currNum > 0 else False
                currNum = num
                ret += 1
            elif flag is not None:
                if flag:
                    if num - currNum < 0:
                        flag = not flag
                        ret += 1
                else:
                    if num - currNum > 0:
                        flag = not flag
                        ret += 1
                currNum = num
        return ret

solve = Solution()
# nums = [1,17,5,10,13,15,10,5,16,8]
# nums = [1,2,3,4,5,6,7,8,9]
# nums = [1,7,4,9,2,5]
# nums = [18, 11, 15, 17, 24, 23]
nums = [0, 0]
print(solve.wiggleMaxLength(nums))
