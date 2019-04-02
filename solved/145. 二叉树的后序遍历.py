"""
没有用递归，和中序差不多。后序的话，先要处理左右两个节点的值（如果存在的话）。如果没有左右节点或者左右节点都已经处理完
再将这个值加入返回数组。我的方法是，在栈中判断栈顶节点的左右节点是否为空，如果为空，将节点值加入返回数组。如果不为空，
先判断右节点是否为空，不为空加入节点数组，再判断左节点是否为空，不为空加入节点数组。最后要将当前节点的左右节点全部设为
空（这点很重呀）。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        if root:
            stack.append(root)
            while stack:
                node = stack[-1]
                if not (node.left or node.right):
                    ret.append(node.val)
                    stack.pop()
                    continue
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                node.right, node.left = None, None
        return ret


tree3 = TreeNode(3)
tree1 = TreeNode(1)
tree2 = TreeNode(2)
tree3.left = tree1
tree3.right = tree2
solve = Solution()
print(solve.postorderTraversal(tree3))
