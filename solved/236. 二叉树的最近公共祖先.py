"""
一般关于树的题目都涉及到递归算法。开始我写的思路是找出是否有存在给的节点。如果有就返回的信息中说明具体是哪个节点。然后在
返回的上层函数中判断是否两个节点都已找到，如果找到了，那么就一路返回上去。
后来，看了别人的解法，觉得自己写的太繁琐了。其实只要返回一个值，这个值是返回的子树中要么有一个给定的节点，要么两个节点都在。
当左右两个子树的返回值都是真时，那么说明当前的节点就是最近公共祖先，然后一路向上返回这个节点。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 有点繁琐
        # def DFS(root, p, q):
        #     pFlag, qFlag, leftP, leftQ, rightP, rightQ = False, False, False, False, False, False
        #     if root == p:
        #         pFlag = True
        #     if root == q:
        #         qFlag = True
        #     if root.left:
        #         leftP, leftQ, leftNode = DFS(root.left, p, q)
        #         if leftNode:
        #             return True, True, leftNode
        #     if root.right:
        #         rightP, rightQ, rightNode = DFS(root.right, p, q)
        #         if rightNode:
        #             return True, True, rightNode
        #
        #     pFlag = pFlag or leftP or rightP
        #     qFlag = qFlag or leftQ or rightQ
        #     if pFlag and qFlag:
        #         return True, True, root
        #     return pFlag, qFlag, None
        #
        # return DFS(root, p, q)[2]

        # 最快解法
        if root == p or root == q:
            return root
        left, right = None, None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        return right