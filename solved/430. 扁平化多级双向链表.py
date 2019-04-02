"""
这一题我看大家的写法都差不多，都是遍历链表时检查有没有子节点，如果有的话，那么使用递归函数检查子节点所在的那个链表，并记录
当前节点的后节点，继续遍历子节点链表。如果某个链表没有子节点，那么返回最后一个节点到上层函数，将返回的节点和原先保留的后节
点联系起来，并继续遍历这一段链表，如果没有结束的话。
注意，在遍历的过程中一定要注意每个节点的各个指针指向。
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head:
            node = head
            self.func(node)
        return head

    def func(self, node):
        while node:
            if node.child:
                post = node.next
                node.next = node.child
                node.child.prev = node
                node.child = None
                last = self.func(node.next)
                last.next = post
                if post:
                    post.prev = last
                node = last
            if not node.next:
                return node
            node = node.next