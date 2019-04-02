"""
我自己写的复杂度为N^2，为一般的解法。使用一个一维的dp数组原数组中某一位的上升子序列的长度，遍历到这一位时，向前遍历，
状态转移方程为dp[i]=min(dp[j]+1)（j<i，且nums[j]<nums[i]），到最后输出dp[n-1]
第二个解法是NlogN的时间复杂度。主体的思想为：先建立一个栈，遍历nums时遇到当前数大于栈顶元素时，就直接入栈；如果小于，
那么就使用二分法查找当前数应该在栈中的位置，然后将该位置的数更改为当前数（其实就是从栈顶开始找到第一个大于当前数的位置，
然后更改）。
"""
class Solution:
    def lengthOfLIS(self, nums):
        # 网上的解法，和我之前做的一题很类似，但我忘了
        # 时间复杂度为NlogN
        if nums:
            stack = [nums[0]]
            for num in nums:
                if num > stack[-1]:
                    stack.append(num)

                else:
                    left, right = 0, len(stack)-1
                    while left < right:
                        mid = (left+right) // 2
                        if stack[mid] > num:
                            right = mid - 1
                        else:
                            left = mid + 1
                    stack[left] = num
                    print(stack)
            return len(stack)
        return 0

        # n^2时间复杂度
        # if not nums:
        #     return 0
        # n = len(nums)
        # dp = [1] * n
        # for i, val in enumerate(nums):
        #     j = i-1
        #     while j >= 0:
        #         if val > nums[j]:
        #             dp[i] = 1 + dp[j] if 1 + dp[j] > dp[i] else dp[i]
        #         j -= 1
        #
        # print(dp)
        # return max(dp)


solve = Solution()
nums = [10,9,2,5,3,7,101,18]
# nums = [-2,-1]
print(solve.lengthOfLIS(nums))