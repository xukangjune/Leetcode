"""
做了几天，终于做完了。感觉方法很笨，还是用到了set去去重的方法。首先我建立了一个字典，字典的键代表的是本次遍历到的数值，然后
值是此数字位置上的递增子序列。每次遍历时，在该位置上再做一次从当前位置向前的遍历，这时候还得建立一个集合，集合里是此次遍历的
值。如果遇到比当前数小的数，先入集合，然后在字典里找到该数的值，加上当前值存入temp数组，如果向前遍历遇到的数子在集合里，就不
用再去操作，直接跳过。更特别的是，如果向前遍历时遇到的数与当前的数相等，也得如上操作然后退出本次循环（遍历）。
字典中的值代表的是，该键最新的递增子序列，所以在第二次向前遍历的时候，每遇到一个数只要操作一次。尤其是遇到相等的数时，该数涵盖
了之前所有的情况，因此没有必要向前继续遍历了。
"""
class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        dp = {}
        print(dp)
        for index, value in enumerate(nums):
            if value not in dp:
                dp[value] = [[value]]
            temp = []
            bag = set()
            for i in range(index-1, -1, -1):
                if nums[i] in bag:
                    continue
                if value >= nums[i]:
                    temp.extend([item + [value] for item in dp[nums[i]]])
                if value == nums[i]:
                    break
            dp[value].extend(temp)
        print(dp)
        for value in dp.values():
            print(value[1:])
            ret += value[1:]
        print(ret)
        ret = list(set(map(tuple, ret)))
        print(ret)
        return list(map(list, ret))


solve = Solution()
# nums = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]
# nums = [4,6,7,7]
nums = [1,1,1,1]
# nums = [1,1,1,2,2,2,3,3,3]
print(solve.findSubsequences(nums))

















