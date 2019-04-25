"""
还是看人家的解法做的，非常巧妙。还有一点我理解错了，这里的子数组应该是在原数组中要连续的，这样就好办多了。可以用两种方法。
1、由于是要连续的，可以先将diff_1 = A[1] - A[0]存下来，然后从2开始遍历数组，如果diff_2 = A[i] - A[i-1],等于diff_1,说明可以构成等差数列。
这时候话要借助dp的帮助，dp可以看成是上一个位置能够构成的等差数列的数量，所以开始为0。然后每次等差数列增加一个数时，先将dp+1，然后加到ret上。要注意
如果等差数列的长度一直在增加，那么dp的数会一直增大。到最后，如果不满足diff_2 != diff_1时，dp归零并且diff_1= diff_2,接着向下遍历。
2、不用每次数组添加一个数就计算一次，可以先计算某一段等差数列的长度，然后直接依靠长度来计算这段等差数列能偶拆成的子数列的数目就🆗了。
"""
class Solution:
    def numberOfArithmeticSlices(self, A):
        n = len(A)
        ret = 0
        if n > 2:
            diff_1 = A[1] - A[0]
            dp = 0
            for i in range(2, len(A)):
                diff_2 = A[i] - A[i-1]
                if diff_1 == diff_2:
                    dp += 1
                    ret += dp
                else:
                    diff_1 = diff_2
                    dp = 0
        return ret


solve = Solution()
A = [1,1,1,3]
print(solve.numberOfArithmeticSlices(A))