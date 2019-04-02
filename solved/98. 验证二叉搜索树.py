"""
这个与普通的二叉搜索树有一点不同，具体有下面两点：节点的左子树只包含小于当前节点的数，节点的右子树只包含大于当前节点的数。
所以我在递归函数的参数中加入了两个边界值，具体的边界值怎样设置全看是哪一个子节点。。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 自己写的, 挺好的
        def judging(node, floor, ceiling):
            rightF, leftF = True, True
            if node.left:
                if floor < node.left.val < node.val:
                    leftF = judging(node.left, floor, node.val)
                else:
                    return False
            if node.right:
                if node.val < node.right.val < ceiling:
                    rightF = judging(node.right, node.val, ceiling)
                else:
                    return False
            return rightF and leftF

        if root:
            floor = float("-inf")
            ceiling = float("inf")
            return judging(root, floor, ceiling)
        return True
