"""
题目中没有给节点的类，所以应该不能再程序中构造新节点。事实上，可以不用构造新的节点。但这样分类就要多一点。
这里我分成了两类：第一类是m=1，第二类是m>1。因为m=1时，要将头节点也倒叙，所以最后不能直接返回原来的头节点。而m>1时，返回
的还是原来的头节点。这两种情况后面有一部分相同，就是在反转m和n之间的节点时，有一部分不同，就是在反转后的这一段链表的前接和后
续节点的不同。
"""
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m != n:
            count = 1
            start = head
            temp = None
            if m == 1:
                prev = start
                post = prev.next
            else:
                while count < m - 1:
                    start = start.next
                    count += 1
                prev = start.next
                post = prev.next
                count += 1
            while count < n:
                temp = post.next
                post.next = prev
                prev, post = post, temp
                count += 1
            if m == 1:
                head.next = temp
                head = prev
            else:
                start.next.next = post
                start.next = prev
        return head