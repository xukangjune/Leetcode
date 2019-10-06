"""此算法遍历一遍数组，并且将之前的数与下标加入到map中，这样在遍历时，如果目标数与当前数之间的差出现在map中，就可以直接
取出，并返回。"""
from collections import defaultdict
class Solution:
    def twoSum(self, nums, target):
        map = defaultdict(int)
        for idx, num in enumerate(nums):
            tmp = target - num
            if tmp in map:
                return [map[tmp], idx]
            else:
                map[num] = idx


a = [2,7,11,15]
t = 9
solve = Solution()
print(solve.twoSum(a, t))
