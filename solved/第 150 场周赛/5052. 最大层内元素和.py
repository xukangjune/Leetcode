# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        ret = 1
        nodes = [root]
        n = 1
        currsum = root.val
        while nodes:
            tmp = []
            tmpsum = sum([node.val for node in nodes])
            if currsum < tmpsum:
                ret = n
                currsum = tmpsum
            for node in nodes:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            nodes = tmp
            n += 1
        return ret