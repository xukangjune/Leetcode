"""
我觉得我写的挺好的，时间复杂度为n，空间复杂度为常数。首先将字符串中所有的1和0的数目记录下来，然后比较这两个数，较小的就是全为0和全为1所需要的最小次
数。然后开始遍历字符串，此时就是要找前面为0后为1这种情况所需要的次数。每次遇到0时，将0前面的1翻成0，后面的0反转成1，这两个操作加起来需要的次数与ret
比较。遇到1时不用操作。每次遍历时，都记录下此刻0和1的数目，因为可以根据全部的01数目计算出后面的01数目。遍历到的1都不用操作，因为遍历到0时会将0前面的
1反转成0，这里就是1已经被操作了。
"""
class Solution:
    def minFlipsMonoIncr(self, S):
        numOfZeros = S.count('0')
        numOfOnes = S.count('1')
        numOfZerosSofar = 0
        numOfOnesSofar = 0
        ret = min(numOfOnes, numOfZeros)
        for num in S:
            if num == '0':
                numOfZerosSofar += 1
                transTimes = numOfOnesSofar + numOfZeros - numOfZerosSofar
                ret = min(ret, transTimes)
            else:
                numOfOnesSofar += 1
        return ret


solve = Solution()
s = "00011000"
print(solve.minFlipsMonoIncr(s))