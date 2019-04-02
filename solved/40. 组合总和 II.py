"""
与第39题思路差不多，知识同一个位置的值不能重复使用。在这里我用的递归函数中的参数没有传入当前的数组，所以需要返回一个数组，然后在回溯的过程中
加到上层函数的数组中，最后返回一个完整的。程序的结尾要去重。
网上的另一种写法是在递归函数中，传入当前的数组，然后某个条件满足时，就直接将当前的数组加入全局变量中。
在这里还有一个小知识点，我在返回时是这样写的：return ret.append([value])，这样写是不对的，因为这是一个赋值语句，赋值语句没有返回值。
"""
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if target in candidates:
            ret.append([target])
        candidates.sort(key=lambda x: x > target)
        candidates = sorted(filter(lambda x: x < target, candidates)) 
        print(candidates, ret)
        def func(candidates, target):
            ret = []
            for index, value in enumerate(candidates):
                if value == target:
                    ret.append([value])
                elif value < target:
                    if index > 0 and candidates[index] == candidates[index-1]:      # 可以增加这一段预先去重
                        continue
                    retList = func(candidates[index+1:], target-value)
                    for returned in retList:
                        returned.append(value)
                        ret.append(returned)
                else:
                    return ret
            return ret
        for returned in func(candidates, target):
            # if returned in ret:   # 去重
            #     continue
            ret.append(returned)

        return ret


solve = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(solve.combinationSum2(candidates, target))