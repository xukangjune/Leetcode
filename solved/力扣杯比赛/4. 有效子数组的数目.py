class Solution:
    def validSubarrays(self, nums):
        ret = 0
        n = len(nums)
        i = 0
        end = float("inf")
        count = 0
        while i < n:
            leftNum = nums[i]
            if leftNum < end:
                count -= 1
                j = end
            j = i
            while j < n and nums[j] >= leftNum:
                count += 1
                j += 1
            ret += count
            end = j




        # def dfs(i, leftNum):
        #     nonlocal ret
        #     if i == n-1:
        #         ret += 1
        #         return
        #     ret += 1
        #     if leftNum <= nums[i+1]:
        #         dfs(i+1, leftNum)
        #
        # for i,num in enumerate(nums):
        #     dfs(i, num)
        # return ret


solve = Solution()
nums = [3,2,1]
print(solve.validSubarrays(nums))