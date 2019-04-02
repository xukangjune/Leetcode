"""
还是用了迭代的方法。先将节点放入栈中，然后循环判断为空。如果为空则结束，如果不为空，那么先拿出最后一个节点，如果当前节点的
右节点，那么插入当前节点的前面，如果当前节点没有左节点（说明当前节点前面已经没有节点了），则将当前节点的值加入返回数组；如
果左节点不为空，那么将左节点加入当前节点后面，重要的是将当前的左右节点最后都赋值为None，这样下一次遇到此节点时（原左子树已
经全部加入了返回数组），因为先头已经设置了左节点为空，此时可以直接加入返回数组。
有一点重要的是，在遇到左右节点都不为空时（或只有左子树时），此时必须将左右节点在加入数组后全部赋值为None。我就是这个没有注
意到，所以开始总是出错。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
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
                if node.right:
                    stack.insert(-1, node.right)
                if not node.left:
                    ret.append(node.val)
                    stack.pop()
                else:
                    stack.append(node.left)
                    node.left = None
                    node.right = None
        return ret


tree3 = TreeNode(3)
tree1 = TreeNode(1)
tree2 = TreeNode(2)
tree3.left = tree1
tree3.right = tree2
solve = Solution()
print(solve.inorderTraversal(tree3))