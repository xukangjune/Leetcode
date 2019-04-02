"""
这一题为了避免后续的麻烦，直接使用了一个新的节点，该节点直接指向head，即给原本的链表多加了一个头。然后，再找出n个节点
之后的节点，接着保持这样一个窗口向后移动，直到到达尾节点。然后进行删除操作。
也可以选择不使用虚结点，可以直接对链表操作，但是有点繁琐。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head and n:
            dummy = ListNode(None)
            dummy.next = head
            head = post = dummy
            for i in range(n):
                post = post.next
            while post and post.next:
                head, post = head.next, post.next
            head.next = head.next.next
            head = dummy.next
        return head