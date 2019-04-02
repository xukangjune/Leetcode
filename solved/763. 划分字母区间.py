"""
稍微改进了一下。还是用到了贪心算法，我先用一个字典的来存储每个S中字母的最后的位置，然后从头遍历字符串，将第一个子母
的最后位置作为截止位置。如果在截止位置之前有字母最后的位置大于截止位置，那么截止位置改变。最后到安全遍历到截止位置时
就说明起始位置到截止位置正常，计算长度加入返回数组，然后继续在截止位置后一位当作新的起始位置，继续遍历原字符串。
"""
class Solution:
    def partitionLabels(self, S):
        ret = []
        lastLetterIndex = {}
        n = len(S)
        for i in range(n):
            lastLetterIndex[S[i]] = i
        i = 0
        while i < n:
            biggestIndex = lastLetterIndex[S[i]]
            j = i
            while j < biggestIndex:
                if lastLetterIndex[S[j]] > biggestIndex:
                    biggestIndex = lastLetterIndex[S[j]]
                j += 1
            ret.append(j-i+1)
            i = j + 1
        return ret


solve = Solution()
S = "ababcbacadefegdehijhklij"
# S = "abaccbdeffed"
# S = 'abcd'
# S =''
print(solve.partitionLabels(S))