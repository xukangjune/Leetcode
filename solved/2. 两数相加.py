"""��ԭ�����㷨���˸Ľ�������û���õ�����Ŀռ䣬��Ϊ���ǵ����ʾ�����Ե�ǰ��p��q���λ��ӡ�Ȼ�󽫽������l1�ϣ�����
���ؽ��Ҳ��l1�������ʹ������⣬�������l1��l2���Ȳ�ͬ���������ô�͵÷�������ǡ����l1�ĳ��Ƚϳ�����ô���Խ���ǰq��
�ڵ�ӵ�p���棬���l1�Ƚϳ�����ô���ò�����
���һ��ע����ǣ����ǵ������һλʱ����������˽�λ����ô�͵�����һλ��"""
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






