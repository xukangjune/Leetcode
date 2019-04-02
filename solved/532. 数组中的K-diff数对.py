class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        if k < 0:
            return ret
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 0
        if k == 0:
            for keys, values in dict.items():
                if values > 0:
                    ret += 1
        else:
            for keys in dict.keys():
                if keys+k in dict:
                    ret += 1
        return ret


solve = Solution()
nums = [3, 1, 4, 1, 5]
k = 0
print(solve.findPairs(nums, k))