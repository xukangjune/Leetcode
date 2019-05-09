class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        ro = l
        l, r = 0, n-1
        while l <= r:
            m = (l + r) // 2
            mid = (m + ro) % n
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = m  + 1
            else:
                r = m - 1
        return False

solve = Solution()
# nums = [2,5,6,0,0,1,2]
# target = 3
nums = [1,3,1,1,1]
target = 3

print(solve.search(nums, target))