"""
题目要求求解子集，说明只要数组内数字一样就说明是同一个子集，比如[1,2]和[2,1]就是同一个子集。这里要避免出现重复子集，所以先要将数组排好序，排序好的
数组中相同的元素会出现在相邻的位置上，这样会很快进行去重。
我的解法是这样的，利用dfs，遍历数组，如果遍历的当前元素在之前（即本次函数的nums中出现过，那么就跳过，因为，包含此数字的所有情况都已处理），接下来
当遍历的位置到达数组尾部时，就返回一个空数组（因为，要将上层函数的数字包含进去）。
"""
class Solution:
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        def dfs(i):
            ret = [[]]
            if i == n:
                return ret
            j = i
            while j < n:
                if j > i and nums[j] == nums[j-1]:
                    j += 1
                    continue
                ans = dfs(j+1)
                for k in ans:
                    ret.append([nums[j]] + k)
                j += 1
            return ret

        return dfs(0)


solve = Solution()
nums = [4,4,4,1,4]
print(solve.subsetsWithDup(nums))