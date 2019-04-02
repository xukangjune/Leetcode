"""
和上一题没有什么区别，就是加了一个路径追踪。本题最大的缺陷就是每次在递归的时候都要进行数组的复制，这一点消耗了大量的内存。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []

        def func(root, sum, path):
            if not root:
                return
            elif not root.right and not root.left and root.val == sum:
                path.append(root.val)
                ret.append(path)
            else:
                path.append(root.val)
                if root.right:
                    func(root.right, sum-root.val, path[:])
                if root.left:
                    func(root.left, sum-root.val, path[:])

        func(root, sum, [])
        return ret

