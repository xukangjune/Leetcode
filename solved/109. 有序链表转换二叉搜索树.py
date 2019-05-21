"""
典型的递归方法的使用。开始我以为只要确保根节点左右子树的高度差小于1就行了，但是后来看每个节点都要这样的要求，所以用了递归的方法。
首先，用快慢指针找到中间节点（快慢指针的思路再预习一遍，首先快慢指针都指向开始节点，然后循环判断快指针以及快指针的下个指针是否为空），此处要设置一个
left指针，每次都指向slow指针的前一个节点。这个指针是用来分割链表用的。找到中间节点后，将链表分成两部分，作为左右子树，带入递归函数。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = fast = head
        left = None
        while fast and fast.next:
            left = slow
            slow = slow.next
            fast = fast.next.next
        left.next = None

        ret = TreeNode(slow.val)
        right = slow.next
        ret.left = self.sortedListToBST(head)
        ret.right = self.sortedListToBST(right)
        return ret