"""
同51题N皇后
"""
class Solution:
    def totalNQueens(self, n):
        self.n = n
        self.ret = 0
        self.left = set()
        self.right = set()
        self.up = set()
        self.findAllPermutations([], 0)
        return self.ret

    def findAllPermutations(self, permutation, level):
        if level == self.n:
            self.ret += 1
            return

        for i in range(self.n):
            if i not in self.up and i - level not in self.left and i + level not in self.right:
                self.up.add(i)
                self.left.add(i - level)
                self.right.add(i + level)
                self.findAllPermutations(permutation + [i], level + 1)
                self.up.remove(i)
                self.left.remove(i - level)
                self.right.remove(i + level)
        return


solve = Solution()
n = 10
ret = solve.totalNQueens(n)
print(ret)