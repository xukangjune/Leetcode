"""
这一题本来想用简单一点的解法来写，即先找出层数，然后找出最后一层的节点数，最后通过计算得出节点数，但是发现还是挺难的，所以
中规中矩先计算每一层的节点数，然后统计。
但是觉得递归的方法还是比较简单的，可以先遍历左子树的左节点高度和右子树左节点的高度，如果高度相同，说明左子树是满的二叉树
直接根据高度求出左子树的所有节点，并递归求解右子树的节点。同样，如果高度不同，说明右子树是满的，直接求解节点数，左子树递归
求解。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 迭代
        # ret = 0
        # if root:
        #     ret += 1
        #     temp = [root]
        #     while temp:
        #         next = []
        #         for node in temp:
        #             if node.left:
        #                 ret += 1
        #                 next.append(node.left)
        #             else:
        #                 return ret
        #             if node.right:
        #                 ret += 1
        #                 next.append(node.right)
        #             else:
        #                 return ret
        #         temp = next
        # return ret

        # 递归
        if root:
            l = self.depth(root.left)
            r = self.depth(root.right)
            return 1 + 2 ** l + self.countNodes(root.right) if l == r else 1 + 2 ** r + self.countNodes(root.left)

    def depth(self, node):
            res = 1
            while node.left:
                res += 1
                node = node.left
            return res