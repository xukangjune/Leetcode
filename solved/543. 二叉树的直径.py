"""
递归就好了，每次将每个节点的左右节点长度算出，然后相加看是否大于ret，每层的递归函数都返回左右节点中较大的加1。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        ret = 0
        def recursive(node):
            nonlocal ret
            left = right = 0
            if node.left:
                left = recursive(node.left)
            if node.right:
                right = recursive(node.right)
            if left + right > ret:
                ret = left + right
            return max(left, right) + 1

        if root:
            recursive(root)
        return ret
