"""
这一题还挺好做的，首先是广度遍历，用列表来存储每一层的节点，然后遍历这些节点，如果有子节点就将子节点假如新的临时列表，每一个节点遍历结束后，
我有两个方案，第一个是用一个临时列表来存储这些节点的val，最后将这个由val构成的临时列表加入ret，但是这样有点浪费空间，所以第二个解法就是当
列表中某个节点操作完成后就直接在原列表中将节点改成节点的val，将这个列表（此时列表中已经没有节点了，只有val）加入ret，再将子节点列表赋给临时
列表，接着遍历。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        temp = [root]
        while temp:
            son = []
            ret.append([node.val for node in temp])
            for node in temp:
                if node.left:
                    son.append(node.left)
                if node.right:
                    son.append(node.right)
            # for i in range(len(temp)):
            #     if temp[i].left:
            #         son.append(temp[i].left)
            #     if temp[i].right:
            #         son.append(temp[i].right)
            #     temp[i] = temp[i].val
            # ret.append(temp)
            temp = son
        return ret


solve = Solution()
node3 = TreeNode(3)
node4 = TreeNode(4)
node2 = TreeNode(2)
node2.left = node3
node2.right = node4
node6 = TreeNode(6)
node5 = TreeNode(5)
node5.right = node6
node1 = TreeNode(1)
node1.left = node2
node1.right = node5
print(solve.levelOrder(node1))