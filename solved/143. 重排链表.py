"""
这题我看了网上的答案，大部分都是将后半部分的链表反转过来，这样做很快，但是我这里用到了一种比较复杂的方法，能够锻炼关于指针方面的知识用到了递归，
所以跑起来比较慢。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        flag = False
        def recursive(nodes, node):
            nonlocal flag
            if node.next:
                nodes.append(node)
                prev = recursive(nodes, node.next)
                if flag:
                    return
                middle = nodes.pop(0)
                if middle != node and middle != prev:
                    middle.next = node
                    prev.next = middle

                else:
                    flag = True
                    if middle == node:
                        prev.next = node
                        node.next = None
                    else:
                        middle.next = None
                    return

            else:
                prev = nodes.pop(0)
                prev.next = node
            return node

        if head and head.next and head.next.next:
            recursive([], head)



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
solve = Solution()
solve.reorderList(node1)
node = node1
while node:
    print(node.val)
    node = node.next
