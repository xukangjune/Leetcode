"""
没什么技巧，就是用字典来存储频率，然后对字典排序
"""
class Solution:
    def topKFrequent(self, nums, k):
        frequency = dict()
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1
        ret = [p[0] for p in sorted(frequency.items(), key=lambda x:x[1], reverse=True)[:k]]
        return ret


solve = Solution()
nums = [1,1,1,2,2,3,3,2,3,2,3]
print(solve.topKFrequent(nums,2))