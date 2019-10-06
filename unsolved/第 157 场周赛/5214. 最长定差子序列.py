from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        map = defaultdict(int)
        for num in arr:
            if num-difference in map:
                map[num] = map[num-difference] + 1
            else:
                map[num] = 1
        return max(map.values())


solve = Solution()
# arr = [1,2,3,4]
# difference = 1
# arr = [1,5,7,8,5,3,4,2,1]
# difference = -2
# arr = [1,3,5,7]
# difference = 1
arr = [1,2,3,4,5,6,7]
difference = 1
print(solve.longestSubsequence(arr, difference))