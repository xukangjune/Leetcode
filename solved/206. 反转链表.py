"""
本题是为了反转链表。可以用递归和迭代两种方法来做（本质一样）。核心思想就是保留当前的节点和当前节点的next，然后将next的next指向当前节点（
实现倒序）。递归的话递归函数中的参数为当前节点和当前节点的next，然后在递归函数中改变指针的指向并进行下一次递归。而迭代的变量也是这两个值。
另外，在完成全部的倒序操作后，原链表的head（新链表的最后一个节点）的next指针要重新变成None，不然会陷入死循环。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 后用迭代
        # if head and head.next:
        #     prev = head
        #     post = head.next
        #     while prev and post:
        #         temp = post.next
        #         post.next = prev
        #         print(post.val, post.next.val)
        #         prev, post = post, temp
        #     head.next = None
        #     head = prev
        # print(head.val)
        # return head

        # 也是迭代，人家的水平高好多
        prev = None
        while head:
            head.next, head, prev = prev, head.next, head
        print(prev.val, prev.next.next.val)
        return prev


    # 先用递归
    #     if head and head.next:
    #         node = self.func(head, head.next)
    #         print(node.val)
    #         head.next = None
    #         head = node
    #     return head
    #
    # def func(self, prev, post):
    #     if post.next:
    #         temp = post.next
    #         post.next = prev
    #         print(post.val, post.next.val)
    #         return self.func(post, temp)
    #     else:
    #         post.next = prev
    #         print(post.val, post.next.val)
    #         return post

solve = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
solve.reverseList(node1)