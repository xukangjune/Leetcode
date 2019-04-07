"""贪心法，先将数字转成数组，然后遍历数组，找出第一个递减的位置，找到后将该位前面的数减一，该位至最后全部改成9.这时候没有结束，接着从零遍历到前面
递减的位置，因为可能刚刚减一的操作破坏了之前的递增序列，所以要重新遍历（开始我就是这里没有处理好）。
关于第一个递减的数之后变9，因为要找比当前数小数，那么前面一位必须减少1，如果后面增加的话就大于当前数了。所以前面数减一后，后面数全部换成9，才是最大的。
"""
class Solution:
    def monotoneIncreasingDigits(self, N):
        num = list(map(int, str(N)))
        i = 1
        temp = len(num)
        while i < temp:
            if num[i] < num[i-1]:
                num[i-1] -= 1
                for i in range(i, len(num)):
                    num[i] = 9
                temp = i
                i = 0
            i += 1
        return int(''.join(str(i) for i in num))


solve = Solution()
n = 332
print(solve.monotoneIncreasingDigits(n))