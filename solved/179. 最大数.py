"""
我写的方法好笨，用到了桶排序，将首数子相同的元素放到同一个桶里，然后对每个桶进行操作，然后将每个桶里的元素补齐到最长元素的长度，在后面直接补桶
的序号，接下来进行排序（补齐之后，排序就比较简单）。
别人的代码只有一行,将所有的数字全部转化为字符串（用map（）函数最简单），然后全部赋值到6位（题目给的数字的最大不会超过6位），注意字符串比较是
比较一个个字符的，这点很重要，所以长度的大小并不会影响相对的顺序。
"""
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # bucket = [[] for i in range(10)]
        # nums = [str(num) for num in nums]
        # ret = ''
        # for num in nums:
        #     bucket[int(num[0])].append(num)
        # for i in range(9, -1, -1):
        #     if bucket[i]:
        #         length = len(max(bucket[i], key=len))
        #         temp = {}
        #         print(bucket[i])
        #         for num in bucket[i]:
        #             if num.ljust(length, str(i)) in temp:
        #                 temp[num.ljust(length, str(i))] = max(temp[num.ljust(length, str(i))] + num, num +
        #                                                       temp[num.ljust(length, str(i))])
        #             else:
        #                 temp[num.ljust(length, str(i))] = num
        #         print(temp)
        #         for key in sorted(temp.keys(), reverse=True):
        #             ret += temp[key]
        # return ret if ret and ret[0] != '0' else '0'

        b = (sorted(map(str, nums), key=lambda s: s * 6, reverse=True))
        print(b)
        return ''.join(sorted(map(str, nums), key=lambda s: s * 6, reverse=True))


solve = Solution()
# nums = [3,991, 54, 30,34,5, 95,9]
# nums = [10,2]
# nums =  [3,30,34,5,9]
# nums = [121,12, 99, 9]
nums = [0, 0]
# nums = [9, 9051,5526,2264,5041,1630,5906,6787,8382,4662,4532,6804,4710,4542,2116,7219,8701,8308,957,8775,4822,396,8995,8597,2304,8902,830,8591,5828,9642,7100,3976,5565,5490,1613,5731,8052,8985,2623,6325,3723,5224,8274,4787,6310,3393,78,3288,7584,7440,5752,351,4555,7265,9959,3866,9854,2709,5817,7272,43,1014,7527,3946,4289,1272,5213,710,1603,2436,8823,5228,2581,771,3700,2109,5638,3402,3910,871,5441,6861,9556,1089,4088,2788,9632,6822,6145,5137,236,683,2869,9525,8161,8374,2439,6028,7813,6406,7519]
print(solve.largestNumber(nums))