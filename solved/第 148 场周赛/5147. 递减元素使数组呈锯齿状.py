class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        ret1 = 0
        ret2 = 0
        n = len(nums)
        prev = [nums[0], nums[0]]
        print(prev)
        for i in range(1, n):
            if i % 2:
                if nums[i] >= prev[0]:
                    ret1 += (nums[i]+1-prev[0])
                    prev[0] -=1
                else:
                    prev[0] = nums[i]
                if nums[i] <= prev[1]:
                    ret2 += (prev[1]+1-nums[i])
                    prev[1] = nums[i]
                else:
                    prev[1] = nums[i]


            else:
                if nums[i] <= prev[0]:
                    ret1 += (prev[0]+1-nums[i])
                    prev[0] = nums[i]
                else:
                    prev[0] = nums[i]
                if nums[i] >= prev[1]:
                    ret2 += (nums[i]+1-prev[1])
                    prev[1] -= 1
                else:
                    prev[1] = nums[i]

            print(prev)

        return min(ret1, ret2)



solve = Solution()
# nums = [9,6,1,6,2]
# nums = [10,4,4,10,10,6,2,3]
# nums = [3,10,7,9,9,3,6,9,4]
nums = [2,7,10,9,8,9]
print(solve.movesToMakeZigzag(nums))
