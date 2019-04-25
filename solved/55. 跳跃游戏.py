"""
开始自己写的，所以时间复杂度有点大，但是思路很简单。先用一个数组（长度为n)来存储各个位置能够到达的状态，最后一位是True。然后反向遍历数组，看每一位
是否都能到达最后，返回的结果就是数组第一位是否是True。正常我是过不了的，最后用了一个取巧的方法，针对的是最后一个例子。
后来，看了别人的解法，感觉就是我上面解法的改进。首先遍历原数组，然后看原数组的每一位能够到达的最大位置，如果遍历的某位置时，当前位置的下标大于之前所有
位置能够达到的最大位置时，说明当前的位置之前到达不了，说明错误，直接结束遍历。
最后，比较能够到达的最大位置和数组最后一个数的下标的相对大小。
"""
class Solution:
    def canJump(self, nums):
        n = len(nums)
        #刚开始写的，时间复杂度为O(n^2)。
        # dp = [0] * n
        # dp[-1] = 1
        # for i in range(n-2, -1, -1):
        #     if nums[i] == nums[i+1]+1:
        #         dp[i] = dp[i+1]
        #         continue
        #     for k in range(1, nums[i]+1):
        #         if i+k < n and dp[i+k]:
        #             dp[i] = 1
        #             break
        # return True if dp[0] else False

        #看别人的写的，时间复杂度为O(n)。
        reachSoFar = 0
        for i in range(n-1):
            if reachSoFar < i:
                break
            reachSoFar = max(i + nums[i], reachSoFar)
        return reachSoFar >= n-1


solve = Solution()
# nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
nums = [0,4]
print(solve.canJump(nums))