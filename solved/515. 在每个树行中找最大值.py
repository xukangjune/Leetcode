"""
本题我用的是BFS，虽然看人家的解答也有用DFS，但是感觉不好。BFS比较直观，我的想法是遍历每一层，先将每一层的第一个节点的val设为最大，然后依次
和后面遍历的节点val比较大小，等到这一层遍历完后，就将最大值加入返回数组中。并且每一次遍历都将子节点存到一个临时数组中了，下次循环遍历的就是
子节点数组。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        nodes = [root]
        while nodes:
            numMax = nodes[0].val
            son = []
            for node in nodes:
                numMax = node.val if node.val > numMax else numMax
                if node.left:
                    son.append(node.left)
                if node.right:
                    son.append(node.right)
            ret.append(numMax)
            nodes = son
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
print(solve.largestValues(node1))