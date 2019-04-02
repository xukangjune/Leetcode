"""
本题是简单题，其实就是来计算数组中1之间0的个数。在两个1之间的0与1的距离可直接将0的长度除2加1（长度为奇数），直接除以2（长
度为偶数）。但是有一点要注意，那就是开头和结尾0的个数。开头的0可以先计算出来，用first表示。结尾的0就是最后的temp，因为
如果最后一直都是0，那么temp就是这些0的个数，而且没有赋给ret（因为循环已经结束）。
"""
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i = 0
        ret = 1
        n = len(seats)
        first = 1
        temp = 1
        # 如果开头是0，记录下开头0的个数
        while seats[i] == 0 and i + 1 < n and seats[i + 1] == 0:
            first += 1
            i += 1
        while i < n:
            temp = 1
            while seats[i] == 0 and i + 1 < n and seats[i+1] == 0:
                temp += 1
                i += 1
            ret = ret if ret > temp else temp
            i += 1
        ret = ret // 2 + 1 if ret % 2 else ret // 2
        print(ret, first, temp)
        return max(ret, first, temp)


solve = Solution()
# seats = [0,0,0,1,0,1]
seats = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
print(solve.maxDistToClosest(seats))