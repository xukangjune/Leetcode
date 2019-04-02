"""
这是上一题的升级。本题先判断链表是否存在环，如果存在环则要找出入口的节点。还是首先用快慢指针找到相遇的节点，如果没有节点
说明该链表没有环，返回None。如果相遇，那么快指针比慢指针多走了一倍的路程。首先，将从起点到入口节点的距离设为a，入口节点
到快慢相遇节点的距离为b，所以慢节点走的距离为a+b，快节点行走的距离为2（a+b）。快节点从起点开始绕过一次环的路程为2（a+b）。
所以从相遇节点继续向前到入口的距离为a，正好等于起点到入口的距离。所以这时候将一个指针放在起点，另一个指针在相遇的节点。然后
两个指针逐次向下运动，则最后运动了a的距离后一定在入口处相遇，那么最终返回该节点解OK了。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNod
        :rtype: ListNode
        """
        # 我自己写的，虽然通过了，但是奇慢。没有用到环形链表的特点。
        # while head:
        #     slow = head
        #     fast = head
        #     while slow.next and slow.next.next:
        #         fast = fast.next
        #         slow = slow.next.next
        #         if fast == slow:
        #             if fast == head:
        #                 return head
        #             break
        #     if slow.next and slow.next.next:
        #         head = head.next
        #     else:
        #         break
        # return None

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None