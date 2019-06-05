"""
很简单的题目，递归，但是先递归右边再递归左边，并且用一个全局变量来记录累加的结果。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    total = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if root.right:
            self.convertBST(root.right)
        root.val += self.total
        self.total = root.val
        if root.left:
            self.convertBST(root.left)
        return root