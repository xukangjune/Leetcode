"""
和208题差不多，这里我字典的键为长度了，所以在搜索时先直接搜索长度，因为.和一个字母相对，所以长度匹配是前提，接下来我写了另外一个函数来逐位比较单词。
"""
class WordDictionary:

    def __init__(self):
        self.map = {}

    def addWord(self, word: str) -> None:
        n = len(word)
        if n not in self.map:
            self.map[n] = set()
        self.map[n].add(word)

    def search(self, word: str) -> bool:
        n = len(word)
        if n in self.map:
            for elem in self.map[n]:
                if self.match(elem, word, n):
                    return True
        return False

    def match(self, elem, word, n):
        for i in range(n):
            if word[i] == '.':
                continue
            if word[i] != elem[i]:
                return False
        return True


solve = WordDictionary()
solve.addWord("bad")
solve.addWord("dad")
solve.addWord("mad")
print(solve.search("pad"))
print(solve.search("bad"))
print(solve.search(".ad"))
print(solve.search("b.."))