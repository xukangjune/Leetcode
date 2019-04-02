"""
这个题目想了好久，开始用二维动态规划做的，很简单的思路，状态转移方程也好写，但是最后的超了空间限制。后来想了一下这个题目的动态
规划的状态转移方程比较简单，即dp[i][j] = dp[i][j-1]*nums[j]，因为下一位置的值只与上一次的位置的有关，而且每个位置的值只
用过一次，所以可以用一个变量来存储上一次的值，这样就大大减小的存储空间。所以最后时间复杂度就变成常数空间。
但是这样做虽然满足了空间限制要求，但是提交时超了时间限制。然后想了一个简单一点的法子，就是在第二层循环中直接将第一层循环遍历的
值nums[i]向后乘，直到最后的乘积大于给定值时nums[j]就停止（因为都是所有数都是正数，所以继续向后乘就没有意义）。停止后直接将
ret+=j-i。这样写最后还是超了时间限制，因为有一个测试用例全部的都是1。1是特殊的情况，因为1乘以其他数后大小不变，所以我就先统计
连续1的个数，首先连续1的中有(1+ones)*ones/2个全部是1的连续数组符合要求（如果目标值k大于1）。然后第二层遍历继续向后遍历，假如
如果后面还有的数小于k，那么最后将（j-i)*(ones+1)，要算上这些数之前的连续1。最后这样做终于通过了所有的测试用例，但是时间还是比较
慢，最后只超过了一半的提交答案。
最后看来安歇比较快的解答，豁然开朗。首先直接将所有的数相乘，每一次外层的遍历都对返回数组进行一次加法操作。因为如果数组的数累乘小于
k的话，那么这个数可以和前面数能够组成满足题意的连续数组。假设外层遍历到了nums[j],并从0开始，那么从0，1，2，3，····，j都可以与j
组成连续数组。共j+1个。如果累乘大于等于k，那么将第一个开始的因数nums[i]去掉，循环判断是否还大于等于并保证i<j。如果小于k后，继续将
j-i+1加入返回值中，并继续外层的遍历。这样的解法是最简单的，最快的。
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 我觉得这个算比较快的了，但是实际上比较慢
        # totally shit
        # ret = 0
        # if k > 1:
        #     n = len(nums)
        #     ones = 0
        #     for i in range(n):
        #         if nums[i] == 1 and i < n:
        #             ones += 1
        #             continue
        #         if ones != 0:
        #             ret += (1 + ones) * ones // 2
        #         if nums[i] < k:
        #             product = 1
        #             j = i
        #             while j < n and product * nums[j] < k:
        #                 product *= nums[j]
        #                 j += 1
        #             ret += (j - i) * (ones + 1) if ones != 0 else j - i
        #         ones = 0
        #     if ones != 0:
        #         ret += (1 + ones) * ones // 2
        # return ret

        # 人家的思路，清晰简单，言简意赅
        ret, product, prev = 0, 1, 0
        n = len(nums)
        for i in range(n):
            product *= nums[i]
            while product >= k and prev <= i:
                product //= nums[prev]
                prev += 1
            ret += i - prev + 1
        return ret


solve = Solution()
# nums = [10,5,2,6]
# nums = []
# nums = [1,1,1,1]
nums = [3,10,10,7,6,3,10,1,4,10,8,10]
k = 260
print(solve.numSubarrayProductLessThanK(nums, k))