"""
原来的解法是建立两个数组，数组记录的是相邻相同元素出现的次数。两个数组分别记录两个字符串，最后比较。先比较大小，如果大小不相等，肯定返回
False。看到了在一种比较快的解法，遍历两个数组，看每一次是否相等。如果相等，两个下标都加1，如果不等，typed的下标加1，最后如果name或typed
遍历完，就退出遍历。这里原解法解出错了，他直接返回是不是name遍历完了，没有考虑typed有没有遍历完。如果typed没有遍历完，而且后面出现了不同于
name最后一位的字符，就得返回错误。其它的，都可以归为返回 i==l1的结果。
"""
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        j = 0
        # 丑陋的代码，愚蠢的思路
        # sumName = []
        # sumTyped = []
        # while i < len(name):
        #     temp = 1
        #     while i+1 < len(name) and name[i] == name[i+1]:
        #         i += 1
        #         temp += 1
        #     else:
        #         i += 1
        #     sumName.append(temp)
        # while j < len(typed):
        #     temp = 1
        #     while j+1 < len(typed) and typed[j] == typed[j+1]:
        #         j += 1
        #         temp += 1
        #     else:
        #         j += 1
        #     sumTyped.append(temp)
        # print(sumName)
        # print(sumTyped)
        # if len(sumTyped) < len(sumName):
        #     return False
        # for i in range(len(sumTyped)):
        #     if sumTyped[i] < sumName[i]:
        #         return False
        # return True

        # 别人家的代码
        l1 = len(name)
        l2 = len(typed)
        while True:
            if i == l1 or j == l2:
                break
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                j += 1
        print(i, j)
        # 这是人家返回的结果，有点不严谨
        # return i == l1
        # 这是我补上的部分
        if j < l2:
            for char in typed[j:]:
                if typed[j-1] != char:
                    return False
        return i == l1


solve = Solution()
# name = "aleex"
# typed = "aalee"
# name = "saeed"
# typed = "ssaaedd"
name = "leelee"
typed = "lleeeleet"
print(solve.isLongPressedName(name, typed))

