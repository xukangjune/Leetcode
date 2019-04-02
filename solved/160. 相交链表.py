"""
此题的关键是先将两个链表规划到相同的长度上。可以先遍历计算链表的长度，然后根据相差的长度，缩短某一个链表。这时候两个链表的长度就相等了，此时，
比较两个链表节点的值，如果相等就返回该节点。如果链表到最后变为空，说明没有相同的节点，返回None。
还有一种解法利用了集合的概念，先将headA所有的节点加入集合，然后遍历headB，看headB的节点是否已经在集合内部了，如果在就说明两个链表存在相同
的节点，如果不存在，就说明没有相同的节点，返回None。
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA = headA
        nodeB = headB
        lengthA = 0
        lengthB = 0

        while nodeA is not None:
            lengthA += 1
            nodeA = nodeA.next
        while nodeB is not None:
            lengthB += 1
            nodeB = nodeB.next
        if lengthA > lengthB:
            diff = lengthA - lengthB
            while diff != 0:
                headA = headA.next
                diff -= 1
        else:
            diff = lengthB - lengthA
            while diff != 0:
                headB = headB.next
                diff -= 1
        while headA is not None and headB is not None and headA.val != headB.val:
            headA = headA.next
            headB = headB.next
        if headA is None or headB is None:
            return
        return headB


solve = Solution()
nodeA = ListNode(1)
nodeB = ListNode(1)
print(solve.getIntersectionNode(nodeA, nodeB).val)
