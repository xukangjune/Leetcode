class Solution:
    def missingElement(self, nums, k):
        n = len(nums)
        for i in range(1, n):
            diff1 = nums[i] - nums[i-1] - 1
            if diff1 < k:
                k -= diff1
            else:
                return nums[i-1] + k
        return nums[-1] + k



solve = Solution()
A = [4,7,9,10]
K = 10
print(solve.missingElement(A, K))