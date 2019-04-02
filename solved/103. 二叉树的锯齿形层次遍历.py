"""
和上一题相比，只不过加了一个数组的反转。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        flag = True
        nodeList = [root]
        while nodeList:
            temp = []
            val = []
            if flag:
                ret.append([node.val for node in nodeList])
            else:
                ret.append([node.val for node in nodeList[::-1]])
            for node in nodeList:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                # if flag:
                #     val.append(node.val)
                # else:
                #     val.insert(0, node.val)
            nodeList = temp
            flag = not flag
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
print(solve.zigzagLevelOrder(node1))
