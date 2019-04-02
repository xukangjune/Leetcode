"""
这道题有好多解法。首先我写的是将所有链表的第一个节点值（如果有的话）放在一个临时的数组中，然后再这个数组中找到最小的值，将这个
最小值当作返回链表的下一个节点，然后找出这个数在临时数组的下标，只是临时数组和链表数组一一对应的，就可以映射到链表数组中，接着
判断对应的链表下一个节点是否为空，如果为空则是一番操作，不是另一番操作。
其实，这道题用暴力法是最简单的，也是最快的。直接将所有链表的所有节点值加入一个数组，然后直接排序。
还有一个就是将所有的链表两两合并，然后将新的链表与下一个链表合并，直到结束。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 这么写反而时间慢，内存大，不如暴力法
        # head = ListNode(None)
        # node = head
        # lists = [l for l in lists if l]
        # if lists:
        #     temp = [node.val for node in lists]
        #     while temp:
        #         num = min(temp)
        #         node.next = ListNode(num)
        #         node = node.next
        #         i = temp.index(num)
        #         if lists[i].next:
        #             lists[i] = lists[i].next
        #             temp[i] = lists[i].val
        #         else:
        #             del lists[i]
        #             del temp[i]
        # return head

        # 暴力法，这种方法是最暴力的也是最快的
        ret = []
        if lists:
            for node in lists:
                while node:
                    ret.append(node.val)
                    node = node.next
            ret.sort()
        return ret