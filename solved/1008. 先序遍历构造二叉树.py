"""
这里我用了两个方法，但是本质是一样的，就是不断的递归左右子树，关键是要找到左右子树的分界点，办法是遍历此递归函数的数组然后找到第一大于根节点值得位置，
劈开就是左右子树得子数组。开始我每次递归函数都是直接复制数组然后直接作为参数。后来改进一下，可以用下标来直接运算，有点像C++，但是要注意得是下标的越界
问题。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        def func(i, j):
            if i > j:
                return
            currentRoot = preorder[i]
            node =TreeNode(currentRoot)
            if i == j:
                return node
            for k in range(i+1, j+1):
                if preorder[k] > currentRoot:
                    node.left = func(i+1, k-1)
                    node.right = func(k,j)
                    return node
            node.left = func(i+1, j)
            return node

        return func(0, len(preorder)-1)


        # 第一种解法，每次递归时都复制了数组，有点浪费
        # if preorder:
        #     print(preorder)
        #     node = TreeNode(preorder[0])
        #     if len(preorder) == 1:
        #         return node
        #     for i in range(len(preorder)):
        #         if preorder[i] > preorder[0]:
        #             node.left = self.bstFromPreorder(preorder[1:i])
        #             node.right = self.bstFromPreorder(preorder[i:])
        #             return node
        #     node.left = self.bstFromPreorder(preorder[1:])
        #     return node


solve = Solution()
preorder = [8,5,1,7,10,12]
# preorder = [4, 5, 7]
print(solve.bstFromPreorder(preorder).right.right.val)