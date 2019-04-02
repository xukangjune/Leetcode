"""
开始我用的方法是递归，采用DFS，即先搜索到叶子节点，然后返回累计计算的叶子节点的值，如果不是叶子节点，则当前节点的值就是左右子树的和，这样一
直遍历，直到最后的根节点就是最后的结果。
后来想用迭代的方法来解，就先生成一个列表来存储各个节点，如果当前节点不是叶子节点，那么将当前节点的值乘上10，然后再加上左右子节点的值再赋值为
左右子节点。如果是叶子节点的话，就直接将节点的值累加到ret中。每次操作的节点都是节点列表的第一个值，每次也都要删除这个值，所以列表的长度最终
会降为零，此时遍历结束。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 使用递归的方法，没有新意
        # def dfs(node, sum):
        #     if node:
        #         sum = sum * 10 + node.val
        #     if not node.left and not node.right:
        #         return sum
        #     left, right = 0, 0
        #     if node.left:
        #         left = dfs(node.left, sum)
        #     if node.right:
        #         right = dfs(node.right, sum)
        #     return left + right
        # if not root:
        #     return 0
        # return dfs(root, 0)

        # 尝试用迭代的方法
        # 但是遍历什么时候结束呢？
        # 建立一个数组，这个数组将会包含所有的节点，所以当数组长度为零时，说明遍历结束
        nodeList = [root]
        ret = 0
        if not root:   # 这里要注意，因为如果是root是None也会传入列表
            return 0
        while nodeList:
            current = nodeList[0]
            if current.left:
                current.left.val += current.val * 10
                nodeList.append(current.left)
            if current.right:
                current.right.val += current.val * 10
                nodeList.append(current.right)
            if not current.left and not current.right:
                ret += current.val
            del nodeList[0]
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
print(solve.sumNumbers(node1))
