from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        ret = 0
        temp = defaultdict(int)
        for dominoe in dominoes:
            temp[tuple(dominoe)] += 1

        for i in range(1, 10):
            for j in range(i,10):
                if i == j:
                    count = temp[(i, j)]
                else:
                    count = temp[(i, j)] + temp[(j, i)]
                ret += (count-1)*count//2
        return ret





solve = Solution()
dominoes = [[1,2],[2,1],[3,4],[5,6],[5,6],[6,5],[2,1], [1,2]]

print(solve.numEquivDominoPairs(dominoes))