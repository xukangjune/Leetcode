class Solution:
    def prevPermOpt1(self, A):
        n = len(A)
        i = n-2
        while i >= 0:
            if A[i] > A[i+1]:
                break
            i -= 1

        if i == -1:
            return A

        j = i+1
        while j < n:
            if A[j] >= A[i]:
                break
            j += 1

        A[i], A[j-1] = A[j-1], A[i]

        return A


solve = Solution()
a = [1]
print(solve.prevPermOpt1(a))