"""
和全排列基本的思路相同，但同第一题相比本题的数组中含有重复数字，所以在执行过程中要进行剪枝操作。具体是这样，在遍历过程中
建立一个集合，将如果此时遍历的数在集合内，那么就直接跳过，否则则对当前数字操作，操作完后加入集合之中。
"""
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ret = []
        if n == 1:
            return [nums]
        bag = set()
        for i in range(n):
            if nums[i] not in bag:
                temp = self.permuteUnique(nums[:i]+nums[i+1:])
                print(temp)
                ret += [[nums[i]] + ele for ele in temp]
                bag.add(nums[i])
        return ret


solve = Solution()
nums = [1,1,2,1]
print(solve.permuteUnique(nums))