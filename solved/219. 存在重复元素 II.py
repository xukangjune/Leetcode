"""
先对几种情况进行判断.
1、如果数组的长度与数组对应的集合的长度相等的话，说明没有重复元素输出错误。
2、如果在情况一不成立的情况下，数组的长度小于K，则像第一种情况一样，判断数组与集合长度的大小。
3、在第一，第二条件都不成立的情况下，使用一个动态的窗口，长度为k，从0开始到length-k结束。如果窗口对应的集合长度小于k，说明有重复元素，输出
True。如果遍历结束都没有结果，输出False。
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        if length - len(set(nums)) == 0:
            return False
        # 没有用字典
        # if length <= k:
        #     return True and length - len(set(nums)) > 0 or False
        # for i in range(length - k):
        #     if k - len(set(nums[i:i+k+1])) >= 0:
        #         return True
        # return False

        # 尝试使用字典，虽然代码量减少，但是比之前慢一点
        dict = {}
        for i in range(length):
            if nums[i] in dict and i - dict[nums[i]] <= k:
                return True
            dict[nums[i]] = i
        return False


solve = Solution()
nums = [99,99]
k = 2
print(solve.containsNearbyDuplicate(nums, k))