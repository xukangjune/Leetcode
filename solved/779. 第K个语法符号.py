class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # 非递归
        # flag = False
        # while N >= 1:
        #     if K == 2 ** (N - 1):
        #         if not flag:
        #             return 0 if N % 2 == 1 else 1
        #         return 1 if N % 2 == 1 else 0
        #     elif K > 2 ** (N - 2):
        #         K %= 2 ** (N - 2)
        #         flag = not flag
        #     N -= 1

        # 递归
        if K == 2 ** (N - 1):
            return 0 if N % 2 == 1 else 1

        elif K > 2 ** (N - 2):
            res = self.kthGrammar(N-1, K % 2**(N-2))
            return 0 if res == 1 else 1
        else:
            return self.kthGrammar(N-1, K)






solve = Solution()
print(solve.kthGrammar(5, 16))