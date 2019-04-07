"""
深度优先搜索加上剪枝算法，问题不难，但是要注意边界问题，就是灭个数字都不能超过9，自己在这方面做的还不是很好。如果没有错误提示，那么很难发现错误。
所以以后做题中，尽量考虑全面，避免错误提示。
"""
class Solution:
    def combinationSum3(self, k, n):
        ret = []
        if k >= n or sum(range(1, k+1)) > n:
            return ret

        ret = []
        def DFS(count, target, temp):
            if count == k:
                if target < 10:
                    temp.append(target)
                    ret.append(temp)
                return
            prev = 0 if not temp else temp[-1]
            b = min(10, n // 2)
            for i in range(prev+1, b):
                if target - i <= i:
                    break
                DFS(count+1, target-i, temp+[i])
            return

        DFS(1, n, [])
        return ret


solve = Solution()
k = 3
n = 15
print(solve.combinationSum3(k, n))