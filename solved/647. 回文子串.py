"""
使用了第五题的结论，网上有更快的，但看不懂/(ㄒoㄒ)/~~/(ㄒoㄒ)/~~/(ㄒoㄒ)/~~，≧ ﹏ ≦≧ ﹏ ≦≧ ﹏ ≦。
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
        charIndex = {}
        for i, char in enumerate(s):
            if char not in charIndex:
                charIndex[char] = []
            else:
                for j in charIndex[char]:
                    if dp[j+1][i-1] or i == j + 1:
                        dp[j][i] = 1
                        n += 1
            charIndex[char].append(i)
        return n


solve = Solution()
s = 'abc'
print(solve.countSubstrings(s))