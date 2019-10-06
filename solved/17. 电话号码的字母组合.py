"""
这里投机取巧用到了标准库的方法，但是看了别人的可以用dfs来做。
"""
from itertools import product
class Solution:
    dict = {"2":"abc", "3":"def", "4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

    def letterCombinations(self, digits):
        ret = []
        if digits:
            ret = [char for char in Solution.dict[digits[0]]]  # 实例化类属性
            for digit in digits[1:]:
                ret = [''.join(i) for i in product(ret, Solution.dict[digit])]
        return ret


    # 另一种方法，用的全排列
    # def letterCombinations(self, digits):
    #     if not digits:
    #         return
    #     map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    #     ret = [""]
    #     while digits:
    #         c = digits[0]
    #         tmp = []
    #         for i in ret:
    #             for j in map[c]:
    #                 tmp.append(i+j)
    #         digits = digits[1:]
    #         ret = tmp
    #
    #     return ret


solve = Solution()
a = "23465"
print(solve.letterCombinations(a))