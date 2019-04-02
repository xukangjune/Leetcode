"""
这一题很简单吧
"""
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        print(row, col)
        if r * c > row * col:
            return nums
        nums = [nums[i][j] for i in range(row) for j in range(col)]
        print(nums)
        ret = [[]] * r
        count = 0
        for i in range(r):
            ret[i] = nums[count:count+c]
            count += c
        return ret


solve = Solution()
nums = [[1,2],[3,4],[5,6],[7,8]]
r = 2
c = 4
print(solve.matrixReshape(nums, r, c))
