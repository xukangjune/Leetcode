"""
直接广度优先遍历，很简单
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root) -> int:
        ret = 0
        if not root:
            return 0
        nodes = [root]
        while nodes:
            ret += 1
            tempNodes = []
            for node in nodes:
                if node.left:
                    tempNodes.append(node.lefet)
                if node.right:
                    tempNodes.append(node.right)
            nodes = tempNodes
        return ret
