"""
虽然一遍过了，但是我觉得应该很快的呀！我用的是动态规划，首先建立二维的动态数组，其中dp[i][j]代表字符串s[i:j+1]是否是字符串，是的话就为1，不是为0。
此外，建立一个辅助的字典，字典的键为遍历到的字符串的字符，值为这些字符在字符串出现的索引的数组。
接下来遍历字符串，如果遍历的字符不在字典中，那么建立一个键值对，并将当前的索引加入数组；如果遍历的字符出现在字典中，那么就用动态转移方程：
dp[i][j] = 1 if dp[i + 1][j - 1] or j == i + 1。并且将此时的回文字符串的长度与已有的长度比较，选出最大者，并记录开始和结束的下标。
最后返回，记录下来的开始和结束下标对应的字符串即可。时间复杂度和空间复杂度都为平方级别。
最快的是Manacher方法（不想看，有时间再看吧/(ㄒoㄒ)/~~）
"""
class Solution:
    def longestPalindrome(self, s):
        if s:
            n = len(s)
            dp = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
            length = 1
            begin, end = 0, 1
            charsIndex = {}
            for j, char in enumerate(s):
                if char in charsIndex:
                    for i in charsIndex[char]:
                        if dp[i + 1][j - 1] or j == i + 1:
                            dp[i][j] = 1
                            if j - i + 1 > length:
                                begin, end = i, j+1
                                length = j - i + 1
                else:
                    charsIndex[char] = []
                charsIndex[char].append(j)
            return s[begin:end]
        return ''


solve = Solution()
# s = "babad"
s = "cbbd"
# s = ''
print(solve.longestPalindrome(s))