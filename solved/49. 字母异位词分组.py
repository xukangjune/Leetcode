"""
首先拥有相同字母的单词肯定排序后是一样的，所以用这个作为键，建立一个字典就好了。相同字母的单词存入同一个键中。
"""
class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        for str in strs:
            tempStr = tuple(sorted(str))
            if tempStr not in dict:
                dict[tempStr] = []
            dict[tempStr].append(str)
        return list(dict.values())


solve = Solution()
s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solve.groupAnagrams(s))