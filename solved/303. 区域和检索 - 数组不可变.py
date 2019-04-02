"""
本来想构造一个二维的数组，数组中每一行代表开始位置，每一列代表结束位置。然后列出状态转移方程，但是这样不仅会消耗大量内存，时间复杂度也为
O（n^2),提交通过不了。
然后看到另一种思路是将数组的每一位元素前的和累加，存在另一个数组中，这样的话就可以利用前n项和来求解。这样时间复杂度和空间复杂度都变成为O（n)。
"""
class NumArray:

    # 这个解法会超时
    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     """
    #     self.nums = nums
    #     self.dp = [[self.nums[i] if i == j else 0 for i in range(len(nums))] for j in range(len(nums))]
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             self.dp[i][j] = self.dp[i][j-1] + self.dp[j][j]
    #     print(self.dp)
    #
    # def sumRange(self, i, j):
    #     """
    #     :type i: int
    #     :type j: int
    #     :rtype: int
    #     """
    #     return self.dp[i][j]

    # 另一种解法
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = nums
        for i in range(1, len(nums)):
            self.sum[i] += self.sum[i-1]
        print(self.sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j] if i == 0 else self.sum[j] - self.sum[i-1]


nums = [-2, 0, 3, -5, 2, -1]
solve = NumArray(nums)
print(solve.sumRange(2,2))

