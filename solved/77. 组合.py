"""
这一题并不难，不直到为什么花了这么长时间，其实我最讨厌的还是边界的判断等。
本题用回溯算法，其中可以用剪枝策略来减少回溯的次数，也即递归的次数。为了防止重复数组的出现，整个程序的遍历方向都是从左到右
的。当最后的只需要一个数字时（count=1），直接将剩余的数组返回。
"""
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []

        def DFS(start, count):
            ret = []
            for i in range(start, n+1):
                if i + count - 1 > n:
                    return ret
                if count == 1:
                    return [[num] for num in range(i, n + 1)]
                ret += [ele + [i] for ele in DFS(i+1, count-1)]
            return ret
        if k == 1:
            return [[num] for num in range(1, n+1)]
        for i in range(1, n+2-k):
            temp = DFS(i+1, k-1)
            ans += [ele+[i] for ele in temp]
        return ans


solve = Solution()
print(solve.combine(4,2))