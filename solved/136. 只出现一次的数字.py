"""
这里用到了位运算，任何一个数与零做异或都保持不变，而任何一个数与相同的两个相同的数做完异或后，都是原来的数保持不变。所以用零和数组中所有的数
做异或，最后的数就是零与数组中唯一出现的数异或的结果，也就是该数本身。
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for num in nums:
            ret ^= num
        return ret


solve = Solution()
nums = [0,1,2,1,2]
print(solve.singleNumber(nums))