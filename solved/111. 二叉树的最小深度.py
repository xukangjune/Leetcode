"""
简单题，没有用递归，直接用的广度优先遍历，有个终止条件是当遇到叶子节点时，就停止遍历了，直接返回ret。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        ret = 0
        nodes = [root]
        while nodes:
            ret += 1
            temp = []
            for node in nodes:
                if not node.left and not node.right:
                    return ret
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            nodes = temp
        return ret