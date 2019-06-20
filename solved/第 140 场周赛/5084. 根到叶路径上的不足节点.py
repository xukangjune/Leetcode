# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def recursive(node, limit):
            if node:
                node.left, l_num = recursive(node.left, limit-node.val)
                node.right, r_num = recursive(node.right, limit-node.val)
                num = node.val + max(l_num, r_num)
                if num >= limit:
                    return node, num
                else:
                    return None, num
            else:
                return None, 0
        ret, _num = recursive(root, limit)
        return ret
