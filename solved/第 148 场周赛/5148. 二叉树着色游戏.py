# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        node_x = None
        nodes = [root]
        while nodes:
            tmpNodss = []
            for node in nodes:
                if node.val == x:
                    node_x = node
                    break
                if node.left:
                    tmpNodss.append(node.left)
                if node.right:
                    tmpNodss.append(node.right)
            nodes = tmpNodss

        def bfs_count(root):
            count = 0
            nodes = [root]
            while nodes:
                tmpNodss = []
                count += len(nodes)
                for node in nodes:
                    if node.left:
                        tmpNodss.append(node.left)
                    if node.right:
                        tmpNodss.append(node.right)
                nodes = tmpNodss
            return count

        parent = bfs_count(node_x)
        left = right  =0
        if node_x.left: left = bfs_count(node_x.left)
        if node_x.right: right = bfs_count(node_x.right)

        return  parent <= n // 2 or left >= right+1 or right >= left + 1


