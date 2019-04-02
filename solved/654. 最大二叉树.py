"""
我开始写的很常规，用递归很快就能写出来。后来，看了别人用的迭代，挺好的。一般这种题目迭代要比递归难上很多。
迭代的方法先建立的了一个栈，然后遍历数组，每遍历一个元素就建立一个节点。当栈为空时，节点直接入栈。当栈不为空，而且遍历的值
比栈顶节点的值小，那么这个节点就是栈顶节点的右节点。如果比栈顶元素的大，那么依次将栈顶元素出栈，并将出栈的节点当作当前节点
的左节点，直到栈顶节点的值大于当前节点值，这是和之前一样，将栈顶节点的右节点设为当前节点。这时候如果栈中节点全部出栈，导致
栈为空时，那么不需要将当前节点如何操作，直接入栈。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 非常常规，用的递归
        # n = len(nums)
        # if n == 0:
        #     return None
        # if n == 1:
        #     return TreeNode(nums[0])
        # split = nums.index(max(nums))
        # root = TreeNode(nums[split])
        # root.left = self.constructMaximumBinaryTree(nums[:split])
        # root.right = self.constructMaximumBinaryTree(nums[split+1:])
        # return root

        # 用的迭代
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and num > stack[-1].val:
                node.left = stack.pop()  # while循环
            if stack:
                node.right = node
            stack.append(node)
        return stack[0]
