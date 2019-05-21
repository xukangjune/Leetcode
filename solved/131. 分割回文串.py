"""
全排列的题目，开始先建立两个集合，分别是回文串的集合和非回文串的集合，然后从第一位开始递归下去（dfs），对于每一个字符串，先考虑后面的字符是否在两个字
符串集合里。如果都不在，那么判断是否为字符串，这里我用了一个辅助函数。递归函数到达最后一位时，将字符串数组加入返回数组中。
"""
class Solution:
    def partition(self, s):
        palindromeSet = set()
        notpalindromeSet = set()
        n = len(s)
        ret = []
        def dfs(i, partition):
            if i == n:
                ret.append(partition)
                return

            for j in range(i, n):
                if s[i:j+1] in palindromeSet:
                    dfs(j+1, partition + [s[i:j+1]])
                elif s[i:j+1] in notpalindromeSet:
                    continue
                elif self.isPalindrome(s, i, j):
                    palindromeSet.add(s[i:j+1])
                    dfs(j+1, partition + [s[i:j+1]])
                else:
                    notpalindromeSet.add(s[i:j+1])

        dfs(0, [])
        return ret

    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


solve = Solution()
s = "aaaaaaaagggggg"
print(solve.partition(s))