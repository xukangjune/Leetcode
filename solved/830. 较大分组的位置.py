"""
看了别人写的代码，和自己的大致差不多，都是从首位开始遍历到最后。我的方法是先看连续的三个是否相等，如果相等就接着向下遍历，看有几位连续的字母，
如果不相等，直接遍历下一位。
"""
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        n = len(S)
        i = 0
        ret = []
        while i < n - 2:
            if S[i] == S[i+1] == S[i+2]:
                first = i
                i += 3
                while i < n and S[i] == S[i-1]:
                    i += 1
                ret.append([first, i-1])
            else:
                i += 1
        return ret


solve = Solution()
S = "nnnhaaannnm"
print(solve.largeGroupPositions(S))