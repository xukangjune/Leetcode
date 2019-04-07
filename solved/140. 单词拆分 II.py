"""
(＠_＠;)用的139题的思路，结果超时了，后来发现虽然时动态规划，但是思路不同。这里用到了记忆化搜索，将之前出现过的字符串以字典的形式存储，其中键为字符串，
值为字符串可以用单词列表中拼凑的种类，每次递归时，将当前的字符串分成s[:i]和s[i:](1<=i<=len(s)+1)两个部分，其中s[:i]在单词列表里，那么只要计算
出是s[i:]中切割的所有种类，最后在前面加上s[:i]就行了，至于怎样找s[i:]所有的字串，只要进行递归s[i:]就好了。每次运算都记下s[:i]在字典中，只要在后面
的递归过程过如果遇到相同的字符串就可以直接返回对应的直就好了。
"""
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def DFS(s):
            if s in memo:
                return memo[s]

            if not s:
                return ['']

            res = []
            for i in range(len(s)+1):
                if s[:i] in wordSet:
                    sublist = DFS(s[i:])
                    for temp in sublist:
                        res.append(s[:i] + ('' if not temp else ' ') + temp)
            memo[s] = res
            return res
        print(memo)
        return DFS(s)



    # 一般的动态规划，会超时
    #     n = len(s)
    #     dp = [[] for i in range(n+1)]
    #     lenDict = dict((word, len(word)) for word in wordDict)
    #     dp[0] = ['begin']
    #     for i in range(1, n+1):
    #         for word in wordDict:
    #             if i >= lenDict[word] and dp[i-lenDict[word]] and s[i-lenDict[word]:i] == word:
    #                 for temp in dp[i-lenDict[word]]:
    #                     dp[i].append(temp+ ' ' + word)
    #     if dp[-1]:
    #         return [temp[6:] for temp in dp[-1]]
    #     return []


solve = Solution()
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(solve.wordBreak(s, wordDict))