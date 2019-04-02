"""
挺佩服我自己能写出这么复杂的东西。题目的意思是在二叉树中找到与给定节点距离为k的所有节点，本题比较难办的一点就是这个距离可以通过父节点，所以
要用到递归。首先，要找到目标节点（二叉树的所有节点值唯一），用的是find函数，使用递归。找到后，开始从找到的节点先向下遍历左右子树，用的是
findTheNode函数，这些子树中可能存在距离为k的节点。接着，返回父节点，由于给定的节点是父节点左右节点之一，所以距离值减一。假如此时距离值已经
为0，说明当前的父节点为符合要求。不然的话就使用findTheNode找寻另一个子树。
"""
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.numLists = []
        self.k = 0

    def distanceK(self, root, target, K):
        self.k = K
        self.find(root, target)
        return self.numLists

    def find(self, root, target):
        left = False
        right = False
        if root is None:
            return False
        elif root == target:
            self.findTheNode(root, self.k)
            return True
        else:
            if root.left is not None:
                left = self.find(root.left, target)
            if root.right is not None:
                right = self.find(root.right, target)

        if left or right:
            self.k -= 1
            if self.k == 0:
                self.numLists.append(root.val)
                return False
            elif left and root.right is not None:
                self.findTheNode(root.right, self.k - 1)
            elif right and root.left is not None:
                self.findTheNode(root.left, self.k - 1)
            return True

    def findTheNode(self, node, count):
        if node is None:
            return
        elif count == 0:
            self.numLists.append(node.val)
            return
        else:
            if node.left is not None:
                self.findTheNode(node.left, count - 1)
            if node.right is not None:
                self.findTheNode(node.right, count - 1)
        return


tree = TreeNode(0)
tree1 = TreeNode(1)
tree3 = TreeNode(3)
tree2 = TreeNode(2)
tree.left = tree2
tree.right = tree1
tree1.left = tree3

solve = Solution()
print(solve.distanceK(tree, tree3, 3))