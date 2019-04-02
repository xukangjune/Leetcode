"""
有点慢，但是我看基本上快点的解法都差不多。我这里使用字典来存储数组中每个数作为根节点时数的个数，但是更快的应该用数组，即建立一个和原数组等
长的数组，并且初始化为1，数组的初始化应该比字典快点。
"""
class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # n = len(A)
        # ret = n
        # dict = {}
        # for num in A:
        #     dict[num] = 1
        # A.sort()
        # for i in range(n):
        #     for j in range(i):
        #         division = A[i] / A[j]
        #         if division in dict:
        #             print(ret)
        #             ret += (dict[division] * dict[A[j]])
        #             dict[A[i]] += (dict[division] * dict[A[j]])
        #             print(ret)
        # return ret

        # 改进，更为简练一点
        dp = {}
        A.sort()
        for index, value in enumerate(A):
            dp[value] = 1
            for j in range(index):
                if value / A[j] in dp:
                    dp[value] += dp[A[j]] * dp[value/A[j]]
        return sum(dp.values()) % (10 ** 9 + 7)


solve = Solution()
A = [2, 4, 5, 8]
print(solve.numFactoredBinaryTrees(A))