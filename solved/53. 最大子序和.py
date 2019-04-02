class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ret = nums[0]
        # temp = 0
        # for i in range(len(nums)):
        #     if ret < 0:
        #         if nums[i] < 0:
        #             ret = max(ret, nums[i])
        #         else:
        #             ret = nums[i]
        #             temp = ret
        #     elif nums[i] >= 0:
        #         temp += nums[i]
        #     else:
        #         ret = max(ret, temp)
        #         temp = 0 if temp + nums[i] <= 0 else temp + nums[i]
        # return max(temp, ret) if max(nums) >= 0 else ret

        ret = nums[0]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp > ret:
                ret = temp
            if temp < 0:
                temp = 0
        return ret


solve = Solution()
nums = [-3,-2,0,-1]
print(solve.maxSubArray(nums))