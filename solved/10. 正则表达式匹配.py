"""
这里两个DP都有一个相同点就是将原来的字符串长度都人为的增加了1.但是第一种更巧妙一点，他把DP下标所代表的字符和原字符
串字符统一起来了，而第二个则不是这样，所以下标方面有点一点偏差。首先DP[i][j]的意思是s中前i个字符与p中前j个字符匹配
是否。所以这与s[i],p[j]不同。s[i]代表前i+1个s字符串的字符。
至于DP为什么要这么设置，因为存在s和p为空字符串的情况dp[0][0]代表s，p都为空是的情况，肯定为True。而如果当作下标，那
么就是s[0]与p[0]是否匹配了。
DP都要比递归快。
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
    # 递归，耗时
    #     return self.match(s, p)
    #
    # def match(self, s, p):
    #     if s == p:
    #         return True
    #     elif len(p) > 1 and p[1] == '*':
    #         if s and (s[0] == p[0] or p[0] == '.'):
    #             return self.match(s, p[2:]) or self.match(s[1:], p)
    #         else:
    #             return self.match(s, p[2:])
    #
    #     elif s and p and (s[0] == p[0] or p[0] == '.'):
    #         return self.match(s[1:], p[1:])
    #
    #     return False


    # 动态规划
    #     s = '&' + s
    #     p = '&' + p
    #     sLength = len(s)
    #     pLength = len(p)
    #     dp = [[False * sLength] for i in range(pLength)]
    #     dp[0][0] = True
    #     for i in range(sLength):
    #         for j in range(1, pLength):  #dp[i][0](1<= i < sLength)一定为False, 因为s不为空，而p为空肯定是不匹配的。
    #             if p[j] != '*':
    #                 dp[i][j] = i >= 1 and dp[i-1][j-1] and (s[i] == p[j] or p[j] == '.')
    #             else:
    #                 dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i] == p[j-1] or p[j-1] == '.'))
    #     return dp[-1][-1]

    # 另一种动态规划
        sLength = len(s) + 1
        pLength = len(p) + 1
        dp = [[False] * pLength for j in range(sLength)]  # dp的下标表示的是几个字符的意思,dp[i][j]代表的是s的i个字符和p的j个字符能否匹配的意思
        dp[0][0] = True  # 空字符串s和空的p一定匹配
        for j in range(1, pLength):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]  # 这里注意P[j-1]是指的p下标为j-1，在dp中的位置就是j。如果是*就可以把p前面的一个字符给去掉

        for i in range(1, sLength):
            for j in range(1, pLength):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == '.')
                else:
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.'))
        print(dp)
        return dp[-1][-1]


solve = Solution()
s = ""
p = ".*.*.*"
print(solve.isMatch(s, p))
