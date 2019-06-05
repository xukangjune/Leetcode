"""
开始用下面的方法写的，即先判断第一个相等的下标，然后从后面开始比较，分几种情况，要写清楚。
后来看到别人的解答，很好，直接在一个窗口内统计单词的频率，然后在s内也拿出同一个大小的窗口，进行字母频率统计，最后比较频率数组的大小是否相等。
"""
class Solution:
    def findAnagrams(self, s: str, p: str):
        # 直接统计字母的频率
        pLen = len(p)
        sLen = len(s)
        if pLen > sLen:
            return []
        pList =[0] * 26
        sList = [0] * 26
        ret = []
        for char in p:
            pList[ord(char) - 97] += 1

        for i in range(pLen-1):
            sList[ord(s[i]) - 97] += 1

        for j in range(pLen-1, sLen):
            sList[ord(s[j]) - 97] += 1
            if sList == pList:
                ret.append(j-pLen+1)
            sList[ord(s[j-pLen+1]) - 97] -= 1
        return ret


        # 虽然通过，但是不够好
        # pLen = len(p)
        # sLen = len(s)
        # pList = sorted(p)
        # ret = []
        # i = 0
        # while i < sLen - pLen + 1:
        #     if sorted(s[i:i+pLen]) == pList:
        #         ret.append(i)
        #         j = i + pLen
        #         while j < sLen:
        #             if s[j] == s[i]:
        #                 ret.append(i+1)
        #                 i += 1
        #                 j += 1
        #             else:
        #                 if s[j] not in p:
        #                     i = j
        #                 break
        #     i += 1
        # return ret


solve = Solution()
# s = "sbsb"
# p = "sb"
s = "abacbabc"
p = "abc"
print(solve.findAnagrams(s, p))