"""
其实和96题类似。不过此题要复杂一点，因为要记录n的节点的具体构成，所以放在字典中存的是从start~end所有情况的总结，之后，如果遇到相同的数就可以直接将
其取出。遍历时，从1一直到end，每个数都对应着左右端的节点情况不一样，所以要遍历，并递归，使用字典来存储，可以减少递归的次数。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        if not n: return []
        nodes = {}
        def recursive(start, end):
            if (start, end) in nodes:
                return nodes[(start, end)]
            if start > end: return [None]
            if start == end: return [TreeNode(start)]
            else:
                ret = []
                for i in range(start, end+1):
                    left = recursive(start, i - 1)
                    right = recursive(i+1, end)
                    for leftNode in left:
                        for rightNode in right:
                            root = TreeNode(i)
                            root.left = leftNode
                            root.right = rightNode
                            ret.append(root)
                nodes[(start, end)] = ret
            return ret

        return recursive(1, n)


solve = Solution()
print(len(solve.generateTrees(3)))