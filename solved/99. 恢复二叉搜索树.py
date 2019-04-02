# coding=gbk
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    front = None
    back =None
    lastNode = TreeNode(-2147483648)
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        #O(1)空间复杂度解法
        self.inOrder(root)
        self.front.val,self.back.val = self.back.val,self.front.val
    def inOrder(self,root):
        if root!=None:
            self.inOrder(root.left)
            if self.front == None and root.val<self.lastNode.val:
                self.front = self.lastNode
            if self.front != None and root.val<self.lastNode.val:
                self.back = root
            self.lastNode=root
            self.inOrder(root.right)

# class Solution:
#     def __init__(self):
#         self.nodes = []
#         self.list = []
#
#     def recoverTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: void Do not return anything, modify root in-place instead.
#         """
#         self.inorder(root)
#         self.list = [node.val for node in self.nodes]
#         self.list.sort()
#         for i in range(len(self.list)):
#             self.nodes[i].val = self.list[i]
#         print(self.nodes)
#         print(self.list)
#
#     def inorder(self, node):
#         if node is None:
#             return
#         else:
#             self.inorder(node.left)
#             self.nodes.append(node)
#             self.inorder(node.right)
#
#     def findTheMin(self, root):


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


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
            root = stringToTreeNode(line);

            ret = Solution().recoverTree(root)

            out = treeNodeToString(root)
            if ret is not None:
                print("Do not return anything, modify root in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()