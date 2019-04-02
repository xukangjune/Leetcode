"""
链表的插入排序，从第一个节点遍历到最后一个节点。首先头节点和尾节点都是指向链表的第一个节点，遍历后面的节点时，如果当前节点的值大于尾节点的值，
那么不用插入，直接移向下一个节点，接着循环；如果当前节点的值小于头节点的值，那么当前节点指向头节点，并且赋值为头节点；如果以上都不能满足，那么
插入的位置在头尾之间，先使用一个循环找出应该插入的位置，随后进行操作。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        tail = head
        curNode = head.next
        while curNode:
            if curNode.val >= tail.val:
                tail = curNode
                curNode = curNode.next
            else:
                tail.next = curNode.next
                if curNode.val <= head.val:
                    curNode.next = head
                    head = curNode
                else:
                    temp = head
                    while temp.next.val < curNode.val:
                        temp = temp.next
                    curNode.next = temp.next
                    temp.next = curNode
                curNode = tail.next
        return head

