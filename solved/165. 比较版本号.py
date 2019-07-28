"""
没有使用分割字符串的方法，直接遍历两个字符串，当两者都遇到点号或尾部时就比较大小。如果其中一个到了尾部，可以接着遍历这个字符串，滨崎每次都与
0比较大小。
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = j = 0
        a = b = ""
        while i < len(version1) and j < len(version2):
            while i < len(version1) and version1[i] != '.':
                a += version1[i]
                i += 1
            while j < len(version2) and version2[j] != '.':
                b += version2[j]
                j += 1
            if int(a) > int(b): return 1
            elif int(a) < int(b): return -1
            i += 1
            j += 1
            a = b = ""

        while i < len(version1):
            while i < len(version1) and version1[i] != '.':
                a += version1[i]
                i += 1
            if int(a) > 0: return 1
            elif int(a) < 0: return -1
            i += 1
            a = ""

        while j < len(version2):
            while j < len(version2) and version2[j] != '.':
                b += version2[j]
                j += 1
            if int(b) > 0: return -1
            elif int(b) < 0: return 1
            j += 1
            b = ""

        return 0


solve = Solution()
# version1 = "7.5.2.4"
# version2 = "7.5.3"
# version1 = "1.01"
# version2 = "1.001"
version1 = ""
version2 = "1.0.0"
print(solve.compareVersion(version1, version2))