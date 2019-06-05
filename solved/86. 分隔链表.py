"""
常规题，借助两个指针，分别指向两种不同的情况。有一点要注意（我就是在这里出了问题），在循环的遍历链表的最后，要将分开的两个链表最后全部指向空。因为，
循环结束后，两个链表的尾部是指向原链表的，这样可能会形成死循环。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        smaller = ListNode(None)
        bigger = ListNode(None)
        currSmall = smaller
        currBig = bigger
        node = head
        while node:
            if node.val < x:
                currSmall.next = node
                currSmall = node
            else:
                currBig.next = node
                currBig = node
            node = node.next
        currSmall.next = None
        currBig.next = None

        curr
        if smaller.next and bigger.next:
            currSmall.next = bigger.next
            return smaller.next
        elif smaller.next:
            return smaller.next
        else:
            return bigger.next


solve = Solution()
node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
print(solve.partition(None, 3))
ret = solve.partition(node1, 3)
while ret:
    print(ret.val)
    ret = ret.next