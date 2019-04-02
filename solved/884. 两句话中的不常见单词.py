"""
这一题没有什么算法，只要掌握字符串的用法就好了。注意，空字符串也是字符串
"""
class Solution:
    def uncommonFromSentences(self, A, B):
        A = A + ' ' + B
        A = A.strip().split(' ')
        A.sort()
        print(A)
        ret = []
        n = len(A)
        if n > 1:
            A += ' '
            print(A)
            flag = True
            for i in range(1, n+1):
                if A[i] != A[i-1]:
                    if flag:
                        ret.append(A[i-1])
                    else:
                        flag = not flag
                if A[i] == A[i-1] and flag:
                    flag = not flag
            return ret
        else:
            return A


# A = "this this apple is sweet"
# B = "this apple is sour"
solve = Solution()
# A = ''
# B = ''
A = "apple apple"
B = "banana"
print(solve.uncommonFromSentences(A, B))