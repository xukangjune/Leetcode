"""
还是比较简单的，就是先对数组排序，然后统计相同数字的长度，也就是个数，然后与num+1先做整除，这个就可以将兔子先分成这么多组，颜色是一样的，然后看还有
没有余数，有的话就凑成一组，这样遍历到最后。注意，遍历完成后，还有做一次循环内的运算，因为循环终止时，最后一组没有计算。这是经常考到的。
"""
class Solution:
    def numRabbits(self, answers):
        if not answers:
            return 0
        n = len(answers)
        answers.sort()
        ret = 0
        tempIndex = 0
        for i in range(1, n):
            if answers[i] == answers[i-1]:
                continue
            else:
                count = i - tempIndex
                ret += count // (answers[tempIndex]+1) * (answers[tempIndex]+1)
                if count % (answers[tempIndex]+1):
                    ret += answers[tempIndex]+1
                tempIndex = i
        count = n - tempIndex
        ret += count // (answers[tempIndex] + 1) * (answers[tempIndex] + 1)
        if count % (answers[tempIndex] + 1):
            ret += answers[tempIndex] + 1
        return ret


solve = Solution()
answers = [1, 1,1, 2]
print(solve.numRabbits(answers))