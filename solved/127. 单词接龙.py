"""
好蠢的方法呀！暴力求解，感觉没有什么技巧，可能本题的就是这样解题的吧！
先将字符串列表转为集合，然后头尾各设一个集合，将头尾的单词放入其中。然后比较这两个集合的长度大小，选择其中较小的那个，遍历，此时再遍历单词的每一位，并
将该位替换成26的字母中的一个，先判断替换后的单词是否在另一个集合中，如果在，返回ret；不在，看单词是否在单词集合中，在就加入临时的集合中，并将原单词
集合中的该单词删除，最后将temp集合赋值给当前遍历的集合。
如果出现两个集合都为空的情况，就返回0，即说明不可能成功。
"""
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        head = set()
        tail = set()
        head.add(beginWord)
        tail.add(endWord)
        wordSet.remove(endWord)
        n = len(endWord)
        ret = 2

        while head and tail:
            if len(head) > len(tail):
                head, tail = tail, head

            temp = set()
            for word in head:
                for i in range(n):
                    for j in range(26):
                        tempWord = word[:i] + chr(97+j) + word[i+1:]
                        if tempWord in tail:
                            return ret
                        if tempWord in wordSet:
                            temp.add(tempWord)
                            wordSet.remove(tempWord)
            ret += 1
            head = temp
        return 0


solve = Solution()
begin = "hit"
end = "hot"
words = ["hot","dot","dog","lot","log","cog"]
print(solve.ladderLength(begin, end, words))