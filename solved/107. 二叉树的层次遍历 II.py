# Definition for a binary tree node.
"""
本题和102题一个套路，只不过结果要反向输出，第一种是使用头递归加上BFS的方法，每一层都先向下递归，后加入返回数组中，这样可以实现逆序输出。还有
一个即直接逆序输出102题的结果。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []

        # 这里使用广度优先遍历并加上头递归（先递归，后操作）
        def bfs(level):
            son = []
            for node in level:
                if node.left:
                    son.append(node.left)
                if node.right:
                    son.append(node.right)
            if son:
                bfs(son)
            ret.append([node.val for node in level])
            return

        if root:
            bfs([root])
        return ret

        # 还有一种方法就是将102题的结果反转，这里不再赘述


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
print(solve.levelOrderBottom(node1))

