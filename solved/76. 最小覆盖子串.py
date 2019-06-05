"""
我的第一个解法虽然通过了，但hi是非常慢。我的想法是，现在s中找到第一个完成的t，然后将t中字母在s中出现的下标全部存到字典的列表中，然后用一个列表存储
所有出现的字母的位置。此时的长度作为第一个初始的长度。接下来接着遍历s，遇到一个在t中出现的字母，就将字典中该字母对应列表中第一个下标在queue中删除（
这里涉及了大量的插入，删除运算，所以很耗时）。然后将此位置插入到字典列表和queue，重新计算此时的长度与先前长度比较，得出小的那一个。
上述算法不好，不经涉及大量的列表运算，所以耗时，另外，由于字典中列表和queue的存在，所以消耗空间也比较大。
后来看了别人的解法，这基本上可以算一个模板，神秘链接（https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems）。
首先在字典（这里用的是collections中的字典模板，方便一点）中存下t中各个字母出现的次数。然后遍历s，对每一个字母，都在字典将其数量减一，并且如果该字母
在字典中的值大于0，那么n减去1。当n等于0时，说明此时t中的所有字母在s中都出现过来，那么就要计算长度了。只要确定左边界就可以了。首先l等于0，当s[l]在
字典中小于0时，说明这些都不在t中出现过，那么得给他们加上1。而不为零时，说明此时为第一个t在s中出现的字母，记录此时的长度。并且也要在字典中给相应得字母
加1（保证下次遇到该字母是能够正确进行），l加上1，n加上1（因为少了前面一个字母了）。接着遍历s。这是个很快的解法。
"""
from collections import defaultdict

class Solution:
    #这个解法是看别人的答案的，快了很多。
    def minWindow(self, s: str, t: str) -> str:
        if s and t:
            charIndex = defaultdict(int)
            n = len(t)
            minL, minR = 0, len(s)+1
            for char in t:
                charIndex[char] += 1

            l = 0
            for r, char in enumerate(s):
                if charIndex[char] > 0:   # 当t中所有的元素在字典中的记录清除后，n就变成了0。
                    n -= 1
                charIndex[char] -= 1

                if n == 0:
                    while charIndex[s[l]] < 0:
                        charIndex[s[l]] += 1
                        l += 1

                    if r - l < minR - minL:
                        minL, minR = l, r

                    n += 1
                    charIndex[s[l]] += 1   # 复原，让charIndex字典中字母重新加1，方便后面再次找到时的减1.
                    l += 1

            return "" if minR == len(s) + 1 else s[minL:minR+1]
        return ""


        # 太慢了
        # if s and t:
        #     charIndex = {}
        #     queue = []
        #     T = set(t)
        #     n = len(t)
        #     count = 0
        #     length = float("inf")
        #     begin, end = 0, 0
        #
        #     for i, char in enumerate(s):
        #         if char in T:
        #             if count != n:
        #                 if char not in charIndex:
        #                     charIndex[char] = []
        #                 if len(charIndex[char]) == t.count(char):
        #                     queue.remove(charIndex[char].pop(0))
        #                     charIndex[char].append(i)
        #                     queue.append(i)
        #                     continue
        #                 charIndex[char].append(i)
        #                 count += 1
        #                 queue.append(i)
        #
        #             else:
        #                 queue.remove(charIndex[char].pop(0))
        #                 charIndex[char].append(i)
        #                 queue.append(i)
        #
        #             if count == n:
        #                 if queue[-1] - queue[0] + 1 < length:
        #                     begin, end = queue[0], queue[-1]
        #                     length = queue[-1] - queue[0] + 1
        #
        #     if count != len(t):
        #         return ""
        #     else:
        #         return s[begin:end + 1]
        # return ""






solve = Solution()
# S = "ADOBECODEBANCSHFBFABFABCJHFEG"
# T = "A"
# S = "B"
S = 'bba'
T = 'ab'
print(solve.minWindow(S, T))