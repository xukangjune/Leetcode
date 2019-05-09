"""
在网上看的思路，然后自己改进了一下。这个解法适用于解N数之和的问题。关键在于将N数之和降维到二数之和，所以首先用了DFS将数组先提取N-2个数出来，最后进行
在剩余的数组中进行二数之和的问题，这个二数之和要注意剔除重复项（我在这上面花了点时间，结合前面做过的二数之和）。最后用的全局变量ret来存储所有的结果。
"""
class Solution:
    def fourSum(self, nums, target):
        ret = []
        nums.sort()

        def dfs(nums, target, N, temp):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:
                bag = set()
                n = len(nums)
                i = 0
                while i < n:
                    if target - nums[i] in bag:
                        ret.append(temp + [target - nums[i], nums[i]])
                        bag.add(nums[i])
                        i += 1
                        while i < n and nums[i-1] == nums[i]:
                            i += 1
                        continue
                    bag.add(nums[i])
                    i += 1

            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or (nums[i-1] != nums[i]):
                        dfs(nums[i+1:], target-nums[i], N-1, temp+[nums[i]])


        dfs(nums, target, 4, [])
        return ret


solve = Solution()
# nums = [5,5,3,5,1,-5,1,-2]
# nums = [1,1,1,1]
nums = [0,0,0,0]
print(solve.fourSum(nums, 0))