"""
分治算法。就是“分而治之”，将一个大问题分解成小问题，然后解决小问题的后，再解决大问题。这题就是分治算法。首先，如果字符串中含有运算符，那么对于每个
运算符都可以将字符串分成两部分，左边和右边。递归返回的左边和右边都是数字，然后根据运算符的不同，将数字两两运算。递归到最后，如果最后的字符串只含有
数字，那么就直接返回数字。
"""
class Solution:
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]

        ret = []
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])

                for leftNum in left:
                    for rightNum in right:
                        if input[i] == '+':
                            ret.append(leftNum + rightNum)
                        elif input[i] == '-':
                            ret.append(leftNum - rightNum)
                        else:
                            ret.append(leftNum * rightNum)
        return ret


solve = Solution()
input = ""
print(solve.diffWaysToCompute(input))