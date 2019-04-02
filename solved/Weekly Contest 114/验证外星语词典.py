class Solution(object):
    dict = {}
    maxlength = 0
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        for index, char in enumerate(order):
            self.dict[char] = index
        self.maxlength = len(max(words, key=lambda x: len(x)))
        return words == sorted(words, key=lambda x: self.countNums(x))

    def countNums(self, word):
        num = 0
        for char in word:
            num = num * 10 + self.dict[char]
        num *= 10 ** (self.maxlength - len(word))
        return num

solve = Solution()
# words = ["word","world","row"]
# order = "worldabcefghijkmnpqstuvxyz"
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(solve.isAlienSorted(words, order))