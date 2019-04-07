"""
好久没做动态规划的题目了，有点生疏。
先简历一个动态数组，长度为字符串长度加1。dp[i]代表的是字符串长度为i时，是否满足被数组内单词完全填满的状态（子问题），所以状态转移方程为
dp[i] = 1 (if i >= lenDict[word] and dp[i-lenDict[word]] and word == s[i-lenDict[word]:i])。
1、i >= lenDict[word]表示当前字符串的一定要大于等于当前单词的长度，小于肯定匹配不了；
2、dp[i-lenDict[word]]表示添加这个单词之前，前面分割的部分也是都在单词列表里的，套不然就不满足；
3、word == s[i-lenDict[word]:i]表示分割的单词有效，与当前单词相等。
只有满足这三个条件，当前长度的字符串才可以正确分割，这样一直遍历到长度为n的时候，如果能分割，那么这个地方就会变成True。
"""
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        lenDict = dict((word, len(word)) for word in wordDict)
        for i in range(1, n+1):
            for word in wordDict:
                if i >= lenDict[word] and dp[i-lenDict[word]] and word == s[i-lenDict[word]:i]:
                    dp[i] = 1
                    break
        return dp[-1] == 1

solve = Solution()
# s = "leetcode"
# wordDict = ["leet", "code"]
# s = "applepenapple"
# wordDict = ["apple", "pen", "ok"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = 'leetcodecod'
# wordDict = ["leet", "cod", "code"]
# s = "aaaaaaa"
# wordDict =  ["aaaa","aa"]
s = "cbca"
wordDict =  ["bc","ca"]
print(solve.wordBreak(s, wordDict))
