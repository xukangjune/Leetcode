"""
这一题我用递归和迭代的方法都做了，递归的方法中，递归函数接受两个数，主要的思想是一般的前序遍历会顺序输出树的节点，
而用改进过的“前序”遍历会倒序输出。所以调用这两个会遍历函数一直比较遍历的节点。如果两个节点都为空，那么返回True，
如果一个节点为空另一个不为空，或两个节点的值不等，那么输出False。如果两个节点的值相等，就调用遍历函数。
迭代先建立了两个列表，分别代表着左右子树的每一层的节点。不过左子树是从左向右排列，右子树从右向左排列节点。而过程
中保证了两个列表的长度一定相同。所以每次都从两个列表中相同的位置拿出节点比较，方法和迭代一样。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        # 递归
        # def recursive(node1, node2):
        #     if not (node1 or node2):
        #         return True
        #
        #     if not (node1 and node2) or node1.val != node2.val:
        #         return False
        #
        #     if node1.val == node2.val:
        #         return recursive(node1.left, node2.right) and recursive(node1.right, node2.left)
        #
        # return recursive(root, root)

        # 迭代
        if not root:
            return True

        left = [root.left]
        right = [root.right]
        while left:
            leftNext = []
            rightNext = []
            for i in range(len(left)):
                if not (left[i] or right[i]):
                    continue

                if not (left[i] and right[i]) or left[i].val != right[i].val:
                    return False

                # 保证了一定是两两出现的
                leftNext += [left[i].left, left[i].right]
                rightNext += [right[i].right, right[i].left]
            left, right = leftNext, rightNext
        return True