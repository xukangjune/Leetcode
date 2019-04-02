"""
本题要考虑的情况比较多，其中一点就是出现重复元素时的处理情况（直接使用长度相减）。在这里我是使用了一个flag标志，来记录出现不同字母的次数，如果大于三或者等于一，
肯定返回False。如果次数等于二，返回True。
本题还可以使用zip()函数，应该简单一点。
"""
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        lenA = len(A)
        lenB = len(B)
        if lenA != lenB or lenA < 2:
            return False
        if A == B:
            return True and len(A) - len(set(A)) > 0 or False
        flag = 1
        index = -1
        for i in range(lenA):
            if A[i] != B[i] and flag < 3:
                if index < 0:
                    index = i
                    flag += 1
                else:
                    if A[i] == B[index] and B[i] == A[index]:
                        flag += 1
                    else:
                        return False
                continue
            elif A[i] != B[i]:
                return False
        return True and flag == 3 or False


solve = Solution()
# A = "aaaaaaabc"
# B = "aaaaaaacb"
A = "aba"
B = "aba"
print(solve.buddyStrings(A, B))