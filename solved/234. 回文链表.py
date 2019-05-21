"""
线性的时间复杂度，那么就只能遍历链表几次，所以先使用快慢指针来找出中间节点。然后将中间节点后面的所有节点全部反转，然后分别从头节点和反转后一部分链表的
头节点（原链表的尾节点）开始遍历，知道头节点链表到空。此时，如果两个节点的值不等，返回false，要不然遍历结束后返回true。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = prev = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None

        node = slow.next
        while node:
            temp = node.next
            node.next = slow
            slow = node
            node = temp

        while head:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True