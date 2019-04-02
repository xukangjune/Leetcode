"""
这一题类似于数组，其实在程序中也确实将字符串变成了数组。这是因为Python的字符串时常量，不能赋值。设置头尾指针，如果都是字母，就调换，如果不
是，指针加一或减一。
"""
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        first = 0
        last = len(S) - 1
        S = list(S)
        while first < last:
            if S[first].isalpha() and S[last].isalpha():
                S[first], S[last] = S[last], S[first]
                first += 1
                last -= 1
            elif S[first].isalpha():
                last -= 1
            else:
                first += 1
        return ''.join(S)


solve = Solution()
S = "Test1ng-Leet=code-Q!"
print(solve.reverseOnlyLetters(S))