"""
第一个版本是自己写的，信了剑指offer的邪，寻找全排列的方法很慢，导致最后的结果很慢。
后来看到别人写的，即先用三个集合分别存储Q所在的列，Q所在的列减去所在的行，Q所在的列加上所在的行。这样每一行遍历所有的列，
然后分别看是否与上面的三个集合有重复值，如果有就说明冲突，接着遍历直至最后返回。假如最后有一个排列满足，那么就用可视化函数
导出图案。
"""
# 自己写的， 比较慢
# class Solution:
#     def solveNQueens(self, n):
#         self.n = n
#         self.ret = []
#         permutation = [i for i in range(self.n)]
#         self.findAllPermutations(permutation, 0)
#         return self.ret
#
#     def findAllPermutations(self, permutation, count):
#         if count == self.n:
#             if self.isLegal(permutation):
#                 self.ret.append(self.visualization(permutation))
#
#         for num in range(count, self.n):
#             permutation[count], permutation[num] = permutation[num], permutation[count]
#             self.findAllPermutations(permutation, count+1)
#             permutation[count], permutation[num] = permutation[num], permutation[count]
#
#     def isLegal(self, permutation):
#         for i in range(self.n):
#             for j in range(i+1, self.n):
#                 if i - j == permutation[i] - permutation[j] or i - j == permutation[j] - permutation[i]:
#                     return False
#         return True
#
#     def visualization(self, permutation):
#         ret = []
#         for i in permutation:
#             ret.append('.'*i + 'Q' + '.'*(self.n-1-i))
#         return ret

class Solution:
    def solveNQueens(self, n):
        self.n = n
        self.ret = []
        self.left = set()
        self.right = set()
        self.up = set()
        self.findAllPermutations([], 0)
        return self.ret

    def findAllPermutations(self, permutation, level):
        if level == self.n:
            self.ret.append(self.visualization(permutation))
            return

        for i in range(self.n):
            if i not in self.up and i - level not in self.left and i + level not in self.right:
                self.up.add(i)
                self.left.add(i-level)
                self.right.add(i+level)
                self.findAllPermutations(permutation+[i], level+1)
                self.up.remove(i)
                self.left.remove(i-level)
                self.right.remove(i+level)
        return

    def visualization(self, permutation):
        ret = []
        for i in permutation:
            ret.append('.'*i + 'Q' + '.'*(self.n-1-i))
        return ret


solve = Solution()
n = 4
ret = solve.solveNQueens(n)
for i in ret:
    print(i)


