"""
首先我写的是使用递归，递归的思想很简单，首先判断当前节点为空，如果为空就直接返回。如果不是为空，就检查左节点，如果存在，那么左节点的next指针
就指向右节点，再判断当前节点的next指针是否存在，如果存在，那么右节点指针就指向下节点的左节点。接下来开始尾遍历，即遍历左右节点。
再网上看的解法没有使用递归，而是用的迭代。先判断当前节点是否为空，不为空，将当前的节点赋值为current，然后堆current节点操作。先判断current
和current.left是否同时存在（很重要），如果是的话，对current的左节点next指针赋值为右节点，再看current的next是否存在，存在据对current的
右节点的next指针赋值。这个节点结束后，current赋值为current.next。开始下一轮的判断。当current为空时，说明这一层的值全部遍历结束了，要到
下一层，所以这一层的循环结束，prev=prev.left（每一层的起点都是最左边的节点）。这样遍历下去，如果某次判断，起点为空说明全部就操作完毕了
"""
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # 使用迭代，充分利用next指针
        prev = root
        while prev:
            current = prev
            while current and current.left:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            prev = prev.left


        # 使用了递归，虽然直观，但是耗时长，所需空间多
        # if not root:
        #     return
        # if root.left:
        #     root.left.right = root.right
        #     if root.next:
        #         root.right.next = root.next.left
        # self.connect(root.left)
        # self.connect(root.right)