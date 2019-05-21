"""
对numRows大于等于2时，先建立一个大小为2*numRows-2大小的字符串列表，然后遍历字符串s，对不同的下标索引，将字符放到列表的不同位置，最后将这个列表
组合输出。
"""
class Solution:
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        n = len(s)
        k = 2*numRows - 2
        ret = ['' for i in range(k)]
        for i in range(n):
            temp = i % k
            if temp < numRows:
                ret[temp] += s[i]
            else:
                ret[k-temp] += s[i]
        return ''.join(ret)


solve = Solution()
s = "ABC"
numRows = 2
print(solve.convert(s, numRows))