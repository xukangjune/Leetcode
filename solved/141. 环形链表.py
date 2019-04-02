"""
本题只是要判断链表中是否存在环，由于事先并不知道环有多长，所以使用快慢指针时要先检测next指针是否为空，如果在某一时刻两个
指针相遇说明有环的存在，返回True。否则就说明无环，返回False。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    return True
        return False
