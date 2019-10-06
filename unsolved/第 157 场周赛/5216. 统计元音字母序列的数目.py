class Solution:
    def countVowelPermutation(self, n: int) -> int:
        A = E = I = O = U = 1

        for i in range(1, n):
            a = E + I + U
            e = A + I
            i = E + O
            o = I
            u = I + O
            A = a
            E = e
            I = i
            O = o
            U = u

        return (A+E+I+O+U) % (10**9+7)


solve = Solution()
print(solve.countVowelPermutation(1000))