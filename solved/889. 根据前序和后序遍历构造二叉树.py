"""
妈蛋，题目看错了。开始我以为要返回一个广度优先遍历的数组，但其实只要返回一个树就好了。
这样一来，题目还是比较简单的，只要正确的将pre和post数组分离，然后将每部分当作递归函数的参数。最后返回的是每个子树。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        n = len(pre)
        if n == 1:
            return TreeNode(pre[0])
        if n == 0:
            return None
        root = TreeNode(pre[0])
        leftVal = pre[1]
        leftInd = post.index(leftVal)
        root.left = self.constructFromPrePost(pre[1:2+leftInd], post[:leftInd+1])
        root.right = self.constructFromPrePost(pre[2+leftInd:], post[leftInd+1:n-1])
        return root


solve = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
print(solve.constructFromPrePost(pre, post).left.right.val)