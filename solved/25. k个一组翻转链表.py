"""
这一题是困难题，看起来很简单，但是要考虑的问题非常多，估计这是困难的地方，不注意就会碰到坑（我是一遍过的，耶耶耶）。
我是先用ret来代表最后返回的链表，这个问题要注意的地方有以下几点：
1、链表的长度小于k，这种情况下就要ret来作为第一个节点；
2、结束遍历后，count的值小于k，那么得反转反转后得链表；
3、所有的情况都要考虑“尾节点”和“头节点”；
4、考虑最后prev和ret的区分使用。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        if k < 2 or not head:
            return head
        ret = prev =  ListNode(0)
        firstNode = head
        node = head
        nextNode = node.next
        count = 1

        while nextNode:
            if count == k:
                if not ret.next:
                    ret.next = node

                else:
                    prev.next = node
                prev = firstNode
                firstNode = nextNode
                node = nextNode
                nextNode = node.next
                count = 1
            else:
                tempListNode = nextNode.next
                nextNode.next = node
                node = nextNode
                nextNode = tempListNode
                count += 1

        if count == k:
            if not ret.next:
                ret.next = node

            else:
                prev.next = node
            firstNode.next = None

        else:
            lastNode = node
            nextNode = node.next
            while node != firstNode:
                tempNode = nextNode.next
                nextNode.next = node
                node = nextNode
                nextNode = tempNode

            if not ret.next:
                ret.next = node
            else:
                prev.next = node
            lastNode.next = None

        return ret.next


solve = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print(solve.reverseKGroup(node1, 5).next.val)