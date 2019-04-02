"""
这一题我先用了比较蠢的暴力解答，虽然通过了但是很慢。一共嵌套了三个循环。
后来看到了别人的解法，觉得很好。先从第三位开始遍历数组，然后将遍历的到的数作为第三条边，在数组中此数之前寻找两个数作为另外
两条边，就根据两条边的和大于第三条边，用一个循环即可完成。
"""
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # totally shit
        # ret = 0
        # bag = {}
        # for num in nums:
        #     bag[num] = bag.get(num, 0) + 1
        # nums = sorted(bag.keys())
        # if nums[0] == 0:
        #     del nums[0]
        # n = len(nums)
        # print(nums, n)
        # print(bag)
        # for k in range(n):
        #     first = nums[k]
        #     print('first ', first, bag[first])
        #     if bag[first] >= 3:
        #         temp = bag[first] * (bag[first] - 1) * (bag[first] - 2) // 6
        #         ret += temp
        #         print('temp1  ', temp)
        #         print('ret1  ', ret)
        #     if bag[first] >= 2:
        #         temp = bag[first] * (bag[first] - 1) // 2
        #         i = 0
        #         print('temp2  ', temp)
        #         while i < n and nums[i] < 2 * first:
        #             if i == k:
        #                 i += 1
        #                 continue
        #             ret += temp * bag[nums[i]]
        #             print(ret)
        #             i += 1
        #     print('ret2  ', ret)
        #     for i in range(k+1, n-1):
        #         for j in range(i+1, n):
        #             if first + nums[i] > nums[j]:
        #                 ret += bag[first] * bag[nums[i]] * bag[nums[j]]
        #                 print(ret)
        #
        #                 print()
        # return ret

        # 另一种比较好的解答
        ret = 0
        n = len(nums)
        nums.sort()
        for i in range(2, n):
            first, last = 0, i-1
            while first < last:
                if nums[first] + nums[last] > nums[i]:
                    ret += last - first
                    last -= 1
                else:
                    first += 1
        return ret

solve = Solution()
nums = [1,2,3,4,5,6]
# nums = [2,2,3,4]
# nums = [2,2,2,2,3,3,3,3,3,4,4,4,4,4,4]
print(solve.triangleNumber(nums))