class Solution:
    def minCostToMoveChips(self, chips) -> int:
        even = 0
        odd = 0
        for chip in chips:
            if chip % 2:
                odd += 1
            else:
                even += 1
        return min(odd, even)


solve = Solution()
chips = [2,2,2,3,3]
print(solve.minCostToMoveChips(chips))