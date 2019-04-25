"""
先将一个字典存储两位数的满足相邻两位之差为K的所有可能情况，其中键为0~9，值为最后一位为键的满足情况的数字，比如N=2，K=1时，12就在键为2的里面。
接下来开始遍历，如果N>2，那么字典的每个数后面就得添加数字，我们可以遍历字典的键，因为接下来的一直到结尾的所有的数字的结尾都在这个范围内。另外最后
可能会出现重复值的情况，所以用了集合去重（也可以在存储时，就直接用集合，在开始就进行去重）。
"""
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]
        ret = []
        dp = dict((i, []) for i in range(0, 10))
        for i in range(1, 10):
            if i - K >= 0:
                dp[i-K].append(i*10+i-K)
            if i + K < 10:
                dp[i+K].append(i*10+i+K)

        key = dp.keys()
        for i in range(2, N):
            temp = dict((i, []) for i in range(0, 10))
            for j in key:
                if j + K < 10:
                    temp[j] += [num * 10 +j for num in dp[j + K]]
                if j - K >= 0:
                    temp[j] += [num * 10 + j for num in dp[j - K]]
            dp = temp

        print(dp)
        for value in dp.values():
            ret += list(set(value))
        return ret

solve = Solution()
n = 4
K = 0
print(solve.numsSameConsecDiff(n, K))