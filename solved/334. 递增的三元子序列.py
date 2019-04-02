"""
有时候能想到好想法，却在一些细节方面没有做到优化。这一题由于只要三个数递增就好了，所以先设置两个数为无穷大，当有数
大于第二个数时说明有三个数递增。假如大于第一个数而小于第二个数，那么就第二个的数替换成num。因为大于second的一定会
大于num，这样就扩大了查找的范围。假如num小于第一个数，那么将first换成num，因为不影响second的取值范围，这样如果
后面的数小于second而大于现在的num，那就将second替换，这样原来的first和second就换成了更小的两个数，这样扩大了查
找的范围。
"""

class Solution:
    def increasingTriplet(self, nums):
        # 没必要用stack
        # n = len(nums)
        # if n < 3:
        #     return False
        # stack = [float("inf"), float("inf")]
        # for num in nums:
        #     if num > stack[1]:
        #         return True
        #     elif stack[0] < num < stack[1]:
        #         stack[1] = num
        #     elif num < stack[0]:
        #         stack[0] = num
        #     print(stack)
        # return False

        # 直接用两个数代替
        first = second = float("inf")
        for num in nums:
            if num > second:
                return True
            elif first < num < second:
                second = num
            elif num < first:
                first = num
        return False


solve = Solution()
nums = [5,10,6,4,3]
print(solve.increasingTriplet(nums))