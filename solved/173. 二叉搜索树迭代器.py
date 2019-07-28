"""
这题另一个解法应该也挺好的，就是将这个树进行改造，即每个节点的右节点都指向比他小的下一节点。这样的话，起始节点就是最小的节点，然后每次next（）的
时候都会当前节点就会指向下一个节点，但是改造树的函数我没有看懂，也不想看了。
另一种解法也比较好，首先将所有的左节点入栈。那么栈顶就是最小的节点。使用next函数的就会出栈，并且将栈顶的右子树的左节点全部使用push函数入栈。这样
就能保证下次使用next时是正确的。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push(root)

    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left



    def next(self) -> int:
        """
        @return the next smallest number
        """
        temp = self.stack.pop()
        self.push(temp.right)
        return temp.val



    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack != []

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


node3 = TreeNode(3)
node7 = TreeNode(7)
node15 = TreeNode(15)
node9 = TreeNode(9)
node20 = TreeNode(20)
node7.left = node3
node7.right = node15
node15.left = node9
node15.right = node20

solve = BSTIterator(node7)

