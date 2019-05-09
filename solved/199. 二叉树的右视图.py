"""
直接用广度优先遍历好了，简单明了
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        nodes = [root]
        ret = []
        while nodes:
            ret.append(nodes[-1].val)
            level = []
            for node in nodes:
                if node.left:
                    level.append(node.left)
                if  node.right:
                    level.append(node.right)
            nodes = level
        return ret