"""对原来的算法做了改进，这里没有用到额外的空间，因为数是倒序表示，所以当前的p、q与进位相加。然后将结果存在l1上，最后的
返回结果也是l1。这样就存在问题，就是如果l1和l2长度不同的情况，那么就得分情况考虑。如果l1的长度较长，那么可以将当前q的
节点接到p后面，如果l1比较长，那么不用操作。
最后一点注意的是，就是当到最后一位时，如果产生了进位，那么就得新增一位。"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        p = l1
        q = l2
        while p and q:
            tmp = p.val + q.val + carry
            carry = tmp // 10
            tmp %= 10
            p.val = tmp
            if not q.next or not p.next:
                break
            p = p.next
            q = q.next

        if not q.next and not p.next:
            if carry:
                last = ListNode(carry)
                p.next = last
            return l1

        if not p.next:
            p.next = q.next
            p = p.next

        else:
            p = p.next

        while p and carry:
            tmp = p.val + carry
            carry = tmp // 10
            tmp %= 10
            p.val = tmp
            if not p.next:
                break
            p = p.next

        if carry:
            last = ListNode(carry)
            p.next = last

        return l1






