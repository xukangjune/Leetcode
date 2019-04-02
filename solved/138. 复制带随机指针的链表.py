"""
这一题用的是剑指上的算法，就是先将拷贝的节点连接到原节点的后面。第二步是对原节点的random节点判断，如果random节点存在，
那么拷贝节点的random节点就是原节点的random节点的next节点。就这样到最后将所有拷贝节点的random节点全部找到。最后一步
就是要将原节点和新节点分离出来，不仅要将新节点连接还要将旧节点与新节点的连接分开。
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        node = head
        while node:
            copy = Node(node.val, node.next, None)
            node.next = copy
            node = copy.next

        node = head
        while node:
            copy = node.next
            if node.random:
                copy.random = node.random.next
            node = copy.next

        node2 = ret = head.next
        head.next = ret.next
        node = head.next
        while node:
            node2.next = node.next
            node2 = node2.next
            node.next = node2.next
            node = node.next

        return ret
