# coding=gbk
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.carry = 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = l1
        sum = l1.val + l2.val
        print(sum)
        temp.val = sum % 10
        print(temp.val)
        self.carry = sum // 10
        print(self.carry)
        next_1, next_2 = l1, l2
        if l1.next is not None and l2.next is not None:
            next_1, next_2 = l1.next, l2.next
            while next_1 is not None and next_2 is not None:
                sum = self.carry + next_1.val + next_2.val
                next_1.val = sum % 10
                self.carry = sum // 10
                print(next_1.next)
                print(next_2.next)
                if next_1.next is None or next_2.next is None:
                    break
                next_1, next_2 = next_1.next, next_2.next

        if next_1.next is not None:
            next_1 = next_1.next
            while next_1 is not None:
                if self.carry == 0:
                    break
                sum = next_1.val + self.carry
                next_1.val = sum % 10
                self.carry = sum // 10
                if next_1.next is None:
                    break
                next_1 = next_1.next
            if self.carry == 1:
                newNode = ListNode(1)
                print(newNode.val)
                next_1.next = newNode
                self.carry = 0

        elif next_2.next is not None:
            next_1.next = next_2.next
            next_2 = next_2.next
            while next_2 is not None:
                if self.carry == 0:
                    break
                sum = next_2.val + self.carry
                next_2.val = sum % 10
                self.carry = sum // 10
                if next_2.next is None:
                    break
                next_2 = next_2.next
            if self.carry == 1:
                newNode = ListNode(1)
                print(newNode.val)
                next_2.next = newNode
                self.carry = 0

        if self.carry == 1:
            newNode = ListNode(1)
            print(newNode.val)
            next_1.next = newNode

        return temp






def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()