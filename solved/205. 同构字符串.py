"""
简单题，双方都要映射，一个用字典，一个用集合就行了。
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        set1 = set()
        for i in range(len(s)):
            if s[i] in map1:
                if map1[s[i]] != t[i]:
                    return False
                continue
            else:
                if t[i] in set1:
                    return False
                map1[s[i]] = t[i]
                set1.add(t[i])
        return True