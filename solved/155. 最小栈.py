"""
这一题没有考虑到栈为空的情况，所以在一些函数中没有必要来判断栈是否为空的情况。另外一点需要注意的是，关于getMin的操作，这里用了一个辅助栈来
存储当前遍历到的最小值。在便利的过程中，要判断遍历到的值与最小值栈栈顶元素的比较，小于等于都要入栈。我这里为了避免判断最小值栈是否为空的情况，
现在栈里加了一个很大的元素（其实，不用这么设置都可以，因为在本题中，肯定都是先入栈后来判断最小元素的）。最后，在pop操作的时候，先要判断当前
pop的值是否是等于最小值栈的，如果是的话，就要删除当前最小值栈的节点值。
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = [100000000000]  # 这个数最好是整数的上限

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.minStack[-1]:
            del self.minStack[-1]
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()