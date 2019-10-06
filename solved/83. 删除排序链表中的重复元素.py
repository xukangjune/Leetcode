"""
简单题，先用一个变量保持当前的节点，然后检查后续的节点，如果和当前节点相同就跳过，如果不同，则当前节点指向该节点，然后当前节点移到下一位。
需要注意的是最后prev节点的next要赋值为None。因为假如链表遍历结束后，仍然有相同的元素，由于没有判断到，所以prev的next没有改变，即指向的是
相同元素的节点。所以最后要改变一下。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            prev = head
            cur = prev.next
            while cur:
                if cur.val != prev.val:
                    prev.next, prev = cur, cur
                cur = cur.next
            prev.next = None
        return head