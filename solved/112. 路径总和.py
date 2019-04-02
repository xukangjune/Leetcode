"""
典型的深度有限搜索，使用递归的思想很简单，首先要清楚，递归结束的条件，这一题有两个。如果当前的子树为空，说明sum还没有达到，这一路就已经到头
了，所以返回False。第二个就是到达了子节点，且sum值正好达到，返回True。由于节点值有正有负，所以要一路搜索下去。递归体就是分别遍历当前节点的
左右子树，这是递归函数的sum值要减去当前的节点值。这两个遍历函数要用或语句连接，因为只要有一路满足条件即可。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        print()
        if not root:  # 这时候子树为空
            return False
        elif not root.left and not root.right and root.val - sum == 0:  # 因为必须要到子节点，所以每到一个子节点都要判断
            return True
        else:  # 其它的情况必须让它一步步遍历下去，因为节点值有负数，所以一直要到最后
            return self.hasPathSum(root.right, sum-root.val) or self.hasPathSum(root.left, sum-root.val)