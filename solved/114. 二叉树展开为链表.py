"""
这一题要让左子树全部添加到右子树上去，所以我选择的是递归。先一直递归下去，到达叶子节点后，先返回到父节点，如果只有右节点的话，就不用改变，接
着返回，如果有左节点的话，这时候就要将左节点移到父节点和右节点之间。此时要注意的是先要找到左节点最后一个右节点（左节点只有右子树，递归的必然
性），这最后一个右节点要保留，因为在移动的过程中它的右节点要赋值为当前父节点的右节点。
"""
# Definition for a binary tree node.
from homemade_module.tree_traversal import preorderTrav, postorderTrav
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def func(node):
            left, right = None, None
            if not node.right and not node.left:
                return node
            if node.left:
                left = func(node.left)
            if node.right:
                node.right = func(node.right)  # 右边的子树保持不变，所以处理后还是赋值给右子树
            if left:   # 左子树必须改变
                last = left
                while last.right:
                    last = last.right
                last.right = node.right
                node.right = left
                node.left = None
            return node

        if not root:
            return
        func(root)


sovle = Solution()
# node3 = TreeNode(3)
# node4 = TreeNode(4)
node2 = TreeNode(2)
# node2.left = node3
# node2.right = node4
node6 = TreeNode(6)
node5 = TreeNode(5)
# node5.right = node6
node5.left = node6
node1 = TreeNode(1)
node1.left = node2
node1.right = node5
preorderTrav(node1)
sovle.flatten(node1)
print()
preorderTrav(node1)
print()
postorderTrav(node1)
print()
print(node1.right.right.right.val)
