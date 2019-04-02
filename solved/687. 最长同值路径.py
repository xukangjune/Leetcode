# coding=gbk
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.longest = 0
        self.root = None

    def longestUnivaluePath(self, root):
        self.root = root
        self.findLongestPath(self.root)
        return self.longest

    def findLongestPath(self, node):
        leftSonMax = 0
        rightSonMax = 0
        if node is None:
            return 0
        if node.left is not None:
            leftSonMax = self.findLongestPath(node.left)
        if node.right is not None:
            rightSonMax = self.findLongestPath(node.right)

        if node.left is not None and node.right is not None:
            if node.val == node.left.val and node.val == node.right.val:
                temp_length = leftSonMax + rightSonMax
                self.longest = temp_length if temp_length > self.longest else self.longest
                return leftSonMax + 1 if leftSonMax > rightSonMax else rightSonMax + 1

            elif node.val == node.left.val:
                temp_length = leftSonMax + 1
                self.longest = temp_length if temp_length > self.longest else self.longest
                return temp_length

            elif node.val == node.right.val:
                temp_length = rightSonMax + 1
                self.longest = temp_length if temp_length > self.longest else self.longest
                return temp_length
            else:
                return 0

        elif node.left is not None:
            if node.val == node.left.val:
                temp_length = leftSonMax + 1
                self.longest = temp_length if temp_length > self.longest else self.longest
                return temp_length
            return 0

        elif node.right is not None:
            if node.val == node.right.val:
                temp_length = rightSonMax + 1
                self.longest = temp_length if temp_length > self.longest else self.longest
                return temp_length
            return 0

        else:
            return 0

tree = TreeNode(3)
newNode = TreeNode(3)
tree.left = newNode
solution = Solution()
print(solution.longestUnivaluePath(tree))