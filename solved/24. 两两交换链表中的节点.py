"""
题目的意思是将链表中相邻的节点交换位置，没有什么难的，就是有点绕。唯一一点要注意的就是开头两个节点的变换（如果有的话）。因为最后要返回head，
所以在变化的过程中，要保持head指向第一个节点。所以变化稍微复杂一点，其余的都还可以，在循环的过程中，如果只有一个节点，就不用处理直接返回。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            temp = head.next.next
            head.next.next = head
            head = head.next
            head.next.next = temp
            prev = head.next
            cur = prev.next
            while cur and cur.next:
                temp = cur.next.next
                prev.next = cur.next
                cur.next.next = cur
                cur.next = temp
                prev = cur
                cur = prev.next
        return head