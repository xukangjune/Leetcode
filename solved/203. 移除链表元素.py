"""
简单题。首先一个循环解决链表头部出现val的节点。然后后面用start复制head，对start遍历，消除后面出现val的节点。注意，第三个while的作用，是为了
去除后面连续出现的val。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        start = head
        while start:
            while (start.next and start.next.val == val):
                start.next = start.next.next
            start = start.next
        return head