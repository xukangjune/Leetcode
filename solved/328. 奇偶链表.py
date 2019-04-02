"""
这一题比较简单，只要两个引用一个指向奇链表末尾，另一个指向偶链表末尾。然后在遍历的时候用一个flag来指明当前的变量属于
偶链表还是奇链表，最后正确的接上各个节点就好了。
在网上看到的另一个解答，比较好，使用跳跃法跳节点。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            even = head
            odd = head.next
            post = odd.next
            flag = True
            while post:
                temp = post.next
                if flag:
                    post.next = even.next
                    even.next = post
                    even = post
                else:
                    odd.next = post
                    odd = post
                flag = not flag
                post = temp
            odd.next = None
        return head


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
print(solve.oddEvenList(node1))