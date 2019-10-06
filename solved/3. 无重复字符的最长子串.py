"""
这一题用了时间复杂度线性的。思路是，先定下一个起始位置currPos为0，长度为length=0，返回值ret=0，遍历字符串，如果字符不在字典charsDict内部，就
将字符加入字典，值为字符所在的位置。如果遍历的字符在字典内，那么将与currPos比较大小，如果大于等于它，那么说明现在从currPos到目前遍历的位置正好是
相等的字符串，将ret与当前的length中挑选一个大的赋给ret。接下来比较关键，将currPos设为charsDict[char]+1，作为新的起始位置，然后将length设为
i - currPos，这里可能比真正的长度小了1，但是后面会给补上的（省去了重复代码）。重要的一点就是每次长度改变时，是两个相同的字符的位置相减。
最后一点注意的是，返回值应该是ret和length 的较大者，因为，遍历结束后，没有将最后的length计算，只能在最后手动比较大小。
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        charsDict = {}
        currPos = 0  #当前段的起点
        length = 0
        ret = 0
        for i, char in enumerate(s):
            if char in charsDict:
                if charsDict[char] >= currPos:  #如果遍历到的字母在map中，但是是上次遗留的值。那么对于本段来说。还是新的值。
                    ret = max(ret, length)
                    currPos = charsDict[char]+1
                    length = i - currPos
            charsDict[char] = i
            length += 1

        return max(ret, length)


solve = Solution()
s = "abcadefgbcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "bbtablud"
print(solve.lengthOfLongestSubstring(s))