"""
首先，要建立一个临时的节点当作返回链表的头节点。在遍历原链表的时候，先拿出当前节点的值，然后观察下一个节点，如果下一个节点
是空，那么说明当前节点是最后一个节点；如果下一个节点的值不等于当前节点的值，说明当前节点的值是唯一的（原链表是排序的），那
么将head接在prev的下一节点。重新将prev赋值为head，head为head的next。如果下一个节点值与当前节点值相等说明当前节点应该
舍去，进入while循环，将连续的节点值相等的节点舍去。此时，head指向下一个不相等的节点 ，并接着后面继续判断。
最后一点要注意的是，在返回之前要将prev的next设为None，避免原链表结尾是相等节点的情况。
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
        new = ListNode(None)
        prev = new
        while head:
            value = head.val
            if not head.next or head.next.val != value:
                prev.next = head
                prev = head
                head = head.next
                continue

            while head.next and head.next.val == value:
                head = head.next
            head = head.next
        prev.next = None
        return new.next


solve = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3_1 = ListNode(3)
node3_2 = ListNode(3)
node4_1 = ListNode(4)
node4_2 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3_1
node3_1.next = node3_2
node3_2.next = node4_1
node4_1.next = node4_2
node4_2.next = node5
print(solve.deleteDuplicates(node1))