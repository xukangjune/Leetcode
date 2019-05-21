"""
比较简单，只要用一个类，然后用字典来存储单词，键为单词的第一个字母
"""
class Trie:

    def __init__(self):
        self.map = dict()

    def insert(self, word: str) -> None:
        if word[0] not in self.map:
            self.map[word[0]] = set()
        self.map[word[0]].add(word)

    def search(self, word: str) -> bool:
        return word[0] in self.map and word in self.map[word[0]]

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] in self.map:
            n = len(prefix)
            for word in self.map[prefix[0]]:
                if word[:n] == prefix:
                    return True
        return False


trie= Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))