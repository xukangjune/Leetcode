"""
问题的关键在与遇到后面的数小于前面的数时，时将前面的数减小，还是将后面的数增大。
第一点是要注意，要改变的数是否是第一个，如果是，那么直接将其赋值为后面的数。其它的将当前的数与前面的第二个数比较，如果是大于，说明三个数的
大小情况是这样的a<=b, b>c, c>a,所以要改变b，使得c>=b（因为已经有c>a了），还得b>=a，所以最好的是令b==a；如果是小于或等于，三个数的
大小排序是这样的a<=b, b>c,c<=a,所以要改变c，使得c>=b,唯一的方法是提高c的值，最简单的就是令c==b。按照上面这样，说明已经完成了一次改变（这
里使用一个flag来记录），所以后面假如在出现前面的数大于后面数的情况，就直接输出False。否则，遍历结束后，输出True。
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = True
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                if flag:
                    if i-1 == 0:
                        nums[i-1] = nums[i]
                    else:
                        if nums[i-2] < nums[i]:
                            nums[i-1] = nums[i-2]
                        else:
                            nums[i] = nums[i-1]
                    flag = False
                    continue
                else:
                    return False
            i += 1
        return True


solve = Solution()
# nums = [3,4,2,3]
# nums = [-1,4,2,3]
# nums = [2,3,3,2,4]
nums = [4,2,3]
# nums = [4,2,1]
print(solve.checkPossibility(nums))