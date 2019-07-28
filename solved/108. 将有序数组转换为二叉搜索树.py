"""
简单题，只要将原数组分开成两部分一直递归下去就行了
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        k = n // 2
        node = TreeNode(nums[k])
        node.left = self.sortedArrayToBST(nums[:k])
        node.right = self.sortedArrayToBST(nums[k+1:])
        return node


