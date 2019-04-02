"""
这一题用到字典，首先遍历nums，将nums中的数字作为字典的key，value数组第一个值是key出现的频率，第二个值是第一次出现的索引，第三个值是最后
一次出现的索引（没有就是False）。然后根据频率排序，第一个就是degree。然后长度是最后一个索引减去第一个索引（记住False是在运算中为0，True
为1）。如果第一个ret为小于等于零，说明degree为1，直接返回1。如果不是，遍历排序好的列表（降序）。degree变小时，直接输出ret。没有则要与
之前的ret比较，最后还要返回ret（防止遍历结束后没有在if内比较）。
"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for index, value in enumerate(nums):
            if value not in dict:
                dict[value] = [1, index, False]
                continue
            dict[value][0] += 1
            dict[value][2] = index
        dictTuple = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        degree = dictTuple[0][1][0]
        print(degree, dictTuple)
        ret = dictTuple[0][1][2] - dictTuple[0][1][1] + 1
        if ret <= 0:
            return 1
        print(ret)
        for i in dictTuple:
            if i[1][0] < degree:
                return ret
            ret = i[1][2] - i[1][1] + 1 if i[1][2] - i[1][1] + 1 < ret else ret
        return ret

solve = Solution()
nums = []
print(solve.findShortestSubArray(nums))