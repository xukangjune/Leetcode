"""
刚开始犯了一个大错误，就是temp的组合，开始想的比较简单，觉得组合就只用一种，但是后来看了网上的解答，即使结果是四
选一，怪自己不够严谨。
解答比较简单，先不断的递归到达叶子节点，到达叶子节点后腰返回，这是注意，返回有两个值，第一个值是取该节点时能够得到
的最大值，第二个值是不取该节点的最大值。返回后，上层函数再次判断，求值。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return max(self.func(root))
        return 0

    def func(self, root):
        lv = rv = (0, 0)
        if root.left:
            lv = self.func(root.left)
        if root.right:
            rv = self.func(root.right)
        root.val += (lv[1] + rv[1])
        temp = max(lv) + max(rv)
        return root.val, temp


solve = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node4.left = node2
node4.right = node3
node2.right = node5
node3.right = node1
print(solve.rob(node4))