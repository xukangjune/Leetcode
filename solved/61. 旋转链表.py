"""
这一题也比较简单，先一遍遍历计算链表的长度，然后k对长度取余，这样会大大减少移动的次数。
然后遍历到n-k的地方，作为断点，后面的一段全部前面，前面的放在末尾。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head and k:
            n = 0
            node = head
            while node:
                n += 1
                node = node.next
            k %= n
            if k:
                i = 1
                node = head
                while i < n - k:
                    node = node.next
                    i += 1
                temp = node.next
                node.next = None
                node = temp
                while node.next:
                    node = node.next
                node.next = head
                head = temp
        return head
