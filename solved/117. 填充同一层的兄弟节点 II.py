"""
这一题和上题的区别就是，本题的二叉树就不是完美二叉树了，所以左子树和右子树可能不会同时出现，情况比较复杂。我开始的写法是，每一层都先用一个列
表存储。当这一层全部存储后，接着遍历列表，使前一个节点的next指针指向下一个（最后一个不用操作），接着将列表的第一元素赋值为prev，即为下一层
层的第一个节点。(原来是其中有个语句位置错了，导致很慢，欠打。😠）
第二种方法比较绕，首先再每一层时有两个变量，一个是head（代表的是下层第一个节点），一个数levelPrev代表的是下层”前一个节点“。每次遍历一层时，
都先要判断head是否为空，如果为空，就把第一个遇到的值赋给它，如果不为空，说明levelPrev说明也不为空，所以levelPrev的next指针指向当前的下层
节点，然后levelPrev赋值为当前的下层节点。
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # 用了一个更加好的方法
        prev = root
        while prev:
            current = prev
            head = None
            levelPrev = None
            while current:
                if current.left:
                    if head:
                        levelPrev.next = current.left
                    else:
                        head = current.left
                    levelPrev = current.left
                if current.right:
                    if head:
                        levelPrev.next = current.right
                    else:
                        head = current.right
                    levelPrev = current.right
                current = current.next
            prev = head

        # 用了数组来存储数据，不合适
        # prev = root
        # while prev:
        #     current = prev
        #     curList = []
        #     while current:
        #         if current.left:
        #             curList.append(current.left)
        #         if current.right:
        #             curList.append(current.right)
        #         current = current.next
        #     for i in range(len(curList)-1):   # 第一次这里的位置没有放好
        #         curList[i].next = curList[i+1]
        #     if curList:
        #         prev = curList[0]
        #     else:
        #         break