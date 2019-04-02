"""
这一题首先在长度上进行筛选，然后建立一个一一对应的字典，在遍历过程中，如果不满足这个字典，就说明这个单词不适合。
"""
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        length = len(words[0])
        lenSet = len(set(pattern))
        ret = []
        for word in words:
            if len(set(word)) != lenSet:
                continue
            dict = {}
            i = 0
            while i < length:
                if pattern[i] in dict:
                    if word[i] != dict[pattern[i]]:
                        break
                else:
                    dict[pattern[i]] = word[i]
                i += 1
            if i == length:
                ret.append(word)
        return ret


solve = Solution()
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
# words = ["a","b","c"]
# pattern = "a"
print(solve.findAndReplacePattern(words, pattern))