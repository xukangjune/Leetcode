"""
我觉得这个比较清晰，至少自己想的。首先也是单调栈，当当前高度大于栈顶高度时就入栈。每次入栈的元素为一个二元数组。第一个数代表当前高度，第二数代表能够
包含当前高度的起点，如果先是递增的话，当前起点都是当前坐标。如果小于栈顶高度，那么出栈，计算面积，直到栈顶高度小于当前高度试试，注意，当前高度入栈时，
起点坐标就是栈顶坐标了。
还有一点就是遍历结束时，还要将栈重新清洗一遍。
"""
class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        n = len(heights)
        ret = 0
        for i, value in enumerate(heights):
            temp = [0,i]
            while stack and stack[-1][0] > value:
                temp = stack.pop()
                ret = max(ret, temp[0] * (i - temp[1]))
            stack.append([value, temp[1]])

        while stack:
            temp = stack.pop()
            ret = max(temp[0] * (n - temp[1]), ret)

        return ret


solve = Solution()
s = [2,1,5,6,2,3]
print(solve.largestRectangleArea(s))