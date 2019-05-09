"""
很简单的题目，别的用了collections包的Counter函数。
"""
class Solution:
    def getHint(self, secret, guess):
        n = len(secret)
        dictSecret = {}
        dictGuess = {}
        countA = 0
        countB = 0
        for i in range(n):
            if secret[i] == guess[i]:
                countA += 1
            else:
                dictSecret[secret[i]] = dictSecret.get(secret[i], 0) + 1
                dictGuess[guess[i]] = dictGuess.get(guess[i], 0) + 1
        for key in dictGuess.keys():
            if key in dictSecret:
                countB += min(dictSecret[key], dictGuess[key])
        return "{}A{}B".format(countA, countB)


solve = Solution()
# secret = "1807"
# guess = "7810"
# secret = "1123"
# guess = "0111"
guess = 'a'
secret = 'b'
print(solve.getHint(secret, guess))