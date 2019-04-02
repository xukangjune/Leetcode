"""
用到了回溯算法，在递归的过程中看是否将上层的值凑成一个子数组，不能就返回False.
"""
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        allSum = sum(nums)
        avg = allSum / k
        if allSum % k or max(nums) > avg:
            return False

        def DFS(i, target):
            if nums[i] == target:
                nums[i] = 0
                return True
            if nums[i] < target:
                for j in range(i-1, -1, -1):
                    if not nums[j] or nums[j] + nums[i] > target:
                        continue
                    res = DFS(j, target-nums[i])
                    if res:
                        nums[i] = 0
                        return True
            return False

        i = len(nums)-1
        nums.sort()
        while i >= 0 and nums[i]:
            res = DFS(i, avg)
            if res:
                i -= 1
                continue
            else:
                return False
        return True



solve = Solution()
# nums = [4, 3, 2, 3, 5, 2, 1]
k = 3
# nums = [2,2,2,2,3,4,5]
nums = [2,3,3,2,2]
print(solve.canPartitionKSubsets(nums, k))