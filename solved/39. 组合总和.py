class Solution:
    def __init__(self):
        self.ret = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 直接暴力求解，没有使用递归，多次在复制数组，所以很慢。
        # ret = []
        # if target in candidates:
        #     ret.append([target])
        # all = [[i] for i in candidates if i < target]
        # while all:
        #     newAll = []
        #     for temp in all[:]:
        #         for candidate in candidates:
        #             if candidate >= temp[-1]:
        #                 new = temp[:]
        #                 new.append(candidate)
        #                 if sum(new) < target:
        #                     newAll.append(new)
        #                 elif sum(new) == target:
        #                     ret.append(new)
        #     all = newAll
        # return ret

        # 使用递归，没有事先将数组排序，所以每次都要判断是否比原数组中的数要大，很浪费时间
    #     for candidate in candidates:
    #         self.func(candidates, target, [candidate])
    #     return self.ret
    #
    # def func(self, candidates, target, temp):
    #     if sum(temp) == target:
    #         self.ret.append(temp)
    #         return
    #     for candidate in candidates:
    #         if candidate >= temp[-1]:
    #             new = temp[:]
    #             new.append(candidate)
    #             if sum(new) <= target:
    #                 self.func(candidates, target, new)

        # 另一种递归, 这种是最快的，最好将递归部分单独写一个函数，因为首先的candidates要排序，如果直接在写的话，就像我下面写的一样，要
        # 多次排序，时间会增加。
        ret = []
        candidates.sort()
        for index, value in enumerate(candidates):
            if value == target:
                ret.append([value])
            elif value < target:
                retList = self.combinationSum(candidates[index:], target-value)
                for returned in retList:
                    returned.append(value)
                    ret.append(returned)
            else:
                return ret
        return ret



solve = Solution()
# candidates = [2,3,4,5,6,7]
# target = 7
# candidates = [2,3,5]
# target = 8
candidates = [8,7,4,3]
target = 5
print(solve.combinationSum(candidates, target))
