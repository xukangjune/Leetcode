# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        def dfs(node):
            if not node:
                return []

            if node.val in to_delete:
                return dfs(node.left) + dfs(node.right)

            ret = [node]
            tmp = [node]
            while tmp:
                next = []
                for curr in tmp:
                    if curr.left:
                        if curr.left.val in to_delete:
                            ret += dfs(curr.left)
                            curr.left = None
                        else:
                            next.append(curr.left)
                    if curr.right:
                        if curr.right.val in to_delete:
                            ret += dfs(curr.right)
                            curr.right = None
                        else:
                            next.append(curr.right)
                tmp = next
            return ret

        return dfs(root)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

solve = Solution()
print(solve.delNodes(node1, [3,5]))