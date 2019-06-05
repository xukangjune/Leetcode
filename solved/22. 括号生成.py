"""
也比较简单，使用递归，然后再递归过程中记录左右括号的数量，根据这个数目的比较来决定递归的进行以及如何递归。
"""
class Solution:
    def generateParenthesis(self, n: int):
        ret = []
        def recursive(brackets, left, right):
            if right == n:
                ret.append(''.join(brackets))
                return

            if left < n:
                recursive(brackets + ['('], left+1, right)

            if left > right:
                recursive(brackets + [')'], left, right+1)

        if n:
            recursive([], 0, 0)
        return ret


solve = Solution()
print(solve.generateParenthesis(4))
