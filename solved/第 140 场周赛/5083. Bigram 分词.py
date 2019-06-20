class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        words = text.split(' ')
        index = set()
        ret = []
        for i in range(len(words)-1):
            if words[i] == first:
                index.add(i)
            elif words[i] == second:
                if i-1 in index:
                    ret.append(words[i+1])
        return ret


solve = Solution()
# text = "alice is a good girl she is a good student"
# first = "a"
# second = "good"
text = "we will we will rock you"
first = "we"
second = "will"
print(solve.findOcurrences(text, first, second))