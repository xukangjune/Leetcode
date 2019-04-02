"""
这一题比较好写，直接使用zip函数进行反组合。比我快的算法用的是暴力解法，首先是将第一个字符串作为对象，从第一位开始取出字符，然后遍历后面的字
符串，检查相同的位置是否是同样的字符，如果都是，就在第一个字符串的基础上在多取一位。如果有不相等的情况出现，就直接退出。
还有一种解法是使用了字符串的find方法，也比较好。
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a = zip(*strs)
        ret = ''
        for i in a:
            if len(set(i)) == 1:
                ret += i[0]
            else:
                break
        return ret


solve = Solution()
strs = ["flower","flow","flight"]
print(solve.longestCommonPrefix(strs))