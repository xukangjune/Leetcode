"""
这道题使用了动态规划以及Minimax的两种思想。因为无论是对手还是自己，都要在自己的回合让自己的分数最大（这样对手的分数最小）（这一点很重要），
所以每次返回时都要用max（）函数，去取选择第一个数或者最后一个数后的最大值，然后返回该值。在递归算法中，根据转移方程max(nums[first] - self.
func(first+1, last, nums), nums[last] - self.func(first, last-1, nums))一步一步递归，缩小数组的大小，到最后如果first==last，就
说明递归结束，返回数组中对应位置的数。这样写，虽然很直观，但是时间复杂度和空间复杂度都比较大。虽然，可以使用一个字典来预先存储不同自数组的最
优解，但是还是比较耗时。
所以接下来的方法，没有递归而是直接使用迭代。先生成一个二维数组dp（实际上是一个三角矩阵），这个数组的行序号代表的是子数组的开始位置，列序号则
是子数组结束位置，比如dp[1][3]，说明该位置的值是原数组的位置从1到3这个子序列的最优解。定义一个dp数组，因为同一个子序列的最优解是不会改变的，
所以预先存储，这样下次调用时就十分快速。具体的迭代方式从原数组的头或者尾都可以。这里我选择的是从结尾开始，一步一步遍历到最前面。由于子序列的
头尾节点重合时，说明给i序列只有一个值，那么就不用递归，可以在生成数组的时候直接声明。在迭代时，不断的使用前面以及计算好的值，这样速度比比较快，
最后返回的时dp[0][length-1]（这个就是原数组）是否大于等于零，等于零算平局。
这里是以自己的角度取展开游戏，所以自己取得数减去对手取得数，如果大于零，说明自己赢了，小于零就输了，等于零就说明平局。这一点直接在递归式中就
可以直接体现，不用自己再去计算。
"""


class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    # 动态规划，但用这种方式写会超出时间限制
    #     first = 0
    #     last = len(nums) - 1
    #     return self.func(first, last, nums) >=0 0
    #
    # def func(self, first, last, nums):
    #     if first == last:
    #         return nums[first]
    #     else:
    #         return max(nums[first] - self.func(first+1, last, nums),
    #                    nums[last] - self.func(first, last-1, nums))

    # 稍微快一点，但是还是要使用递归，使用一个字典来预先存储每一段的最优解。
    #     dict = {}
    #     def func(nums):
    #         if len(nums) == 1:
    #             return nums[0]
    #         elif str(nums) in dict:
    #             return dict[str(nums)]
    #         else:
    #             result = max(nums[0] - func(nums[1:]), nums[-1] - func(nums[:len(nums)-1]))
    #             dict[str(nums)] = result
    #             return result
    #     return func(nums) >= 0

    # 网上看的解法，也是动态规划，但是没有使用递归，而是使用了迭代。
        if not nums:
            return True
        length = len(nums)
        dp = [([0] * length) for i in range(length)]
        for i in range(length):
            dp[i][i] = nums[i]
        for left in range(length-2, -1, -1):
            for right in range(left+1, length):
                dp[left][right] = max(nums[left] - dp[left+1][right], nums[right] - dp[left][right-1])
        print(dp)
        return dp[0][length-1] >= 0


solve = Solution()
nums = [1, 5, 2]
print(solve.PredictTheWinner(nums))