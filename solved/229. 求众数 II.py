"""
本题先利用集合计算列表所有的不重复元素，然后使用count方法。
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        length = len(nums)
        if length > 0:
            threshold = length // 3
            a = set(nums)
            for i in a:
                if nums.count(i) > threshold:
                    ret.append(i)
        return ret


solve = Solution()
nums = [1,1,2,1,-1,-1,-1,3]
print(solve.majorityElement(nums))