class Solution:
    def heightChecker(self, heights):
        new = sorted(heights)
        n = len(heights)
        ret = 0
        for i in range(n):
            if heights[i] != new[i]:
                ret += 1
        return ret


solve = Solution()
a = [1,1,4,2,1,3]
print(solve.heightChecker(a))