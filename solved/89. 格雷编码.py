"""
有求格雷码的公式，但这题的目的不是这个。[00, 01, 11, 10]是按格雷码的要求排布的，下一个添加可以按照逆序在每一个数前面加1，即[010, 111, 101, 100]
这样是最方便的，也很快。
学到一个小技巧，当需要利用当前的数组取生成新的数组时，可以记录下当前数组的长度，然后又此长度作为界限，不断往数组中添加元素。虽然，此时的长度在改变，但
由于先前记录的长度，所以不会产生影响。
"""
class Solution:
    def grayCode(self, n: int):
        ret = [0]
        for i in range(n):
            k = 2 ** i
            n = len(ret)-1
            while n >= 0:
                ret.append(ret[n] + k)
                n -= 1
        return ret



solve = Solution()
print(solve.grayCode(2))