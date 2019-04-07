"""
开始写的DFS耗时太长，通过不了。后来改用DP，很快。首先得将nums排序，建立动态数组dp。dp的没一个数表明凑成下标时的种类，dp[0]=1，为特殊项。接下来开
始遍历到n，每次都要遍历nums。如果能够出现num<=i，说明i可能被被凑到，只要看dp[i-num]是否存在。每次只要判断num是否小于等于当前数就好了，因为数字
可以重复出现，而且顺序不同算作不同的序列，所以可以一直向后加num，只要不超过target就行了。"""
class Solution:
    def combinationSum4(self, nums, target):
        nums.sort()
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
                else:
                    break
        return dp[-1]


        # DFS超时
        # nums.sort()
        # ret = 0
        # def DFS(target, path):
        #     nonlocal ret
        #     for num in nums:
        #         if num == target:
        #             ret += 1
        #             return
        #         if num > target:
        #             return
        #         DFS(target-num, path+[num])
        #
        # DFS(target, [])
        # return ret


solve = Solution()
nums = [4,2,1]
target = 32
print(solve.combinationSum4(nums, target))