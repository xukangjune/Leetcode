from collections import defaultdict
class Solution:
    def countCharacters(self, words, chars: str) -> int:
        if chars == '':
            return 0
        ret = 0
        counts = [0] * 26
        for char in chars:
            counts[ord(char)-97] = chars.count(char)

        print(counts)

        for word in words:
            n = len(word)
            i = 0
            while i < n:
                if word.count(word[i]) > counts[ord(word[i])-97]:
                    break
                i+=1
            if i == n:
                ret += n

        return ret


solve = Solution()
# words = ["hello","world","leetcode"]
# chars = "welldonehoneyr"
words = ["cat","bt","hat","tree"]
chars = ""
print(solve.countCharacters(words, chars))