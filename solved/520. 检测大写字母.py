"""
挺简单的一题，只要注意题目的条件就行。
"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if ord(word[0]) > 96:
            for char in word:
                if ord(char) < 91:
                    return False
            return True
        if ord(word[0]) < 91:
            if ord(word[1]) > 96:
                for char in word[1:]:
                    if ord(char) < 91:
                        return False
                return True
            for char in word[1:]:
                if ord(char) > 96:
                    return False
            return True


solve = Solution()
word = "GQQQQi"
print(solve.detectCapitalUse(word))