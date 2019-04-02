"""
本来我想到的就是使用二进制来计算，总共的情况有2 ** len(nums)种。由于输出的二进制长度不确定，所以对二进制字符串从后向前遍历，然后遇到1就
将对应于nums这一位提出，是零就跳过。
另一种方法是使用dfs来解答，要注意每次对ret操作时，要先复制一个数组，然后对这个数组操作。不然会陷入死循环。
"""
class Solution:
    ret = []
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 我自己写的使用二进制来计算的
        length = len(nums)
        ret = []
        for num in range(2**length):
            temp = []
            num = '{0:{1}b}'.format(num, length)
            for index, value in enumerate(num):
                if value == '1':
                    temp.append(nums[index])
            ret.append(temp)
        return ret

        # 下面使用dfs来计算
        # ret = [[]]
        # for num in nums:
        #     for temp in ret[:]:
        #         new = temp[:]
        #         new.append(num)
        #         ret.append(new)
        # return ret

        # 使用递归
    #     self.func(0, nums, [])
    #     return self.ret
    #
    # def func(self, depth, nums, temp):
    #     if depth == len(nums):
    #         self.ret.append(temp)
    #         return
    #     else:
    #         self.func(depth+1, nums, temp[:])
    #         temp.append(nums[depth])
    #         self.func(depth+1, nums, temp)


solve = Solution()
nums = [1,2,3]
print(solve.subsets(nums))