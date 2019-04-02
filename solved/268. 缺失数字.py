"""
这一题是求一个序列中缺失的数。我开始的做法是先求出原序列中最大数求其前N项和，然后减去原序列的代数和。但是该方法有个缺陷，当最后结果等于0时，
不知道有没有缺少零。所以在网上找到一个更高效的解法。先算出序列的长度，然后计算该长度的前N项和，减去序列的总和。此时如果结果等于零，就说明
原序列少了零。（数学知识很重要！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！）
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int(len(nums)*(len(nums)+1)/2) - sum(nums)
        # ret = sum(range(max(nums)+1)) - sum(nums)
        # if ret == 0:
        #     return 0 if 0 not in nums else max(nums)+1
        # return ret


solve = Solution()
a = [0]
print(solve.missingNumber(a))
