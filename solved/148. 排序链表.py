"""
TMD，这题我之前做过，竟然忘了，ＴＭＤ。看到有人写归并链表三部曲：１、快慢指针寻找中间节点，２、使用递归分别处理左右链表，３、调用函数合并左右
两个链表。其中最主要的就是快慢指针寻找中间节点，很有趣。就是先设置一个中间节点和尾节点。尾节点总是比中间节点多走一步，所以总的来看，如果尾节点
到达链表的尾部，那么中间节点就是指向链表的中间节点，所以就将链表分成了两个部分，在分别对这两部分进行递归操作，重复上述的步骤。当链表只有一个
节点时就可以直接返回了。返回后的，要将左右两个已经有序的链表合并成一个有序的链表，常规操作。先申请一个头节点和一个尾节点，头节点指向的是合并的
链表，尾节点直接向的是当前合并链表的尾部节点。比较左右两个链表的每个节点值，谁小就加入合并链表。一直比较下去，最后返回头节点的ｎｅｘｔ。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        midNode = head
        curNode = midNode.next
        while curNode:
            curNode = curNode.next
            if curNode:
                midNode = midNode.next
                curNode = curNode.next
        rightList = midNode.next
        midNode.next = None
        leftList = head
        return self.mergeList(self.sortList(leftList), self.sortList(rightList))

    def mergeList(self, listA, listB):
        newList = ListNode(None)
        tail = newList
        while listA and listB:
            if listA.val <= listB.val:
                tail.next = listA
                listA = listA.next
            else:
                tail.next = listB
                listB = listB.next
            tail = tail.next
        if listA:
            tail.next = listA
        else:
            tail.next = listB
        return newList.next