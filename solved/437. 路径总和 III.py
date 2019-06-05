"""
一次递归，但是内存消耗较大，因为每次递归都记录下了此路径上的所有的值，然后每个递归函数返回当前节点路径上的目标值个数以及左右子树上的节点个数。
使用双递归，一个递归函数只检查以当前节点开始向下路径值，另一个递归将递归所有的节点进行前一个递归函数的运行。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum: int) -> int:
        def recursive(node, sums):
            left = right = 0
            temp = [num+node.val for num in sums] + [node.val]
            if node.left:
                left = recursive(node.left, temp)
            if node.right:
                right = recursive(node.right, temp)
            return temp.count(sum) + left + right

        if root:
            return recursive(root, [])
        return 0
