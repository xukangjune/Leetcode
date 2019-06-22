"""
简单题，用递归一直递归到最下面，然后判断左右子树的高度差是多少，如果大于1，那么返回-1.上层函数接收到-1后，就知道了下面子树高度差大于1，所以直接
也返回-1.最后，如果整个函数返回-1，说明为False，反之大于0，就是True。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            leftValue = rightValue = 0
            if node.left:
                leftValue = dfs(node.left)
            if node.right:
                rightValue = dfs(node.right)
            if leftValue < 0 or rightValue < 0 or abs(leftValue - rightValue) > 1:
                return -1
            return max(leftValue, rightValue) + 1
        if not root: return True
        return True if dfs(root) > 0 else False