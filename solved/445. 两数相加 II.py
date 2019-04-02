"""
我觉得我这个解答都比较复杂了，没想到还有更复杂的。我的思想是先遍历两个链表的长度，在其中挑选比较长的，然后将长的链表一直
遍历到和短链表相同的长度，然后遍历两个链表，将相应的节点值相加。最后一步是调用递归函数依次检查长链表节点值是否超过10，超
过就返回1（carry）。然后一直遍历完长链表。如果最后的carry仍然等于1，则要申请一个新的节点，然后该节点指向长链表，最后返
回该节点。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = n2 = 0
        node1 = l1
        node2 = l2
        while node1:
            n1 += 1
            node1 = node1.next
        while node2:
            n2 += 1
            node2 = node2.next
        if n2 > n1:
            l1, l2 = l2, l1
            n1, n2 = n2, n1
        node1, node2 = l1, l2
        count = 0
        while count < n1 - n2:
            node1 = node1.next
            count += 1
        while node2:
            node1.val += node2.val
            node1, node2 = node1.next, node2.next
        if self.func(l1):
            head = ListNode(1)
            head.next = l1
            return head
        return l1

    def func(self, l1):
        if l1.next:
            carry = self.func(l1.next)
        else:
            temp = l1.val
            l1.val %= 10
            return temp // 10
        temp = l1.val + carry
        l1.val = temp % 10
        return temp // 10
