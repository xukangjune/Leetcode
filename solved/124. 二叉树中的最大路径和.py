# coding=gbk
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.max = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is not None:
            self.max = root.val
        self.findMax(root)
        return self.max

    def findMax(self, node):
        leftSonMax = 0
        rightSonMax = 0

        if node is None:
            return 0
        if node.left is not None:
            leftSonMax = self.findMax(node.left)
        if node.right is not None:
            rightSonMax = self.findMax(node.right)

        if node.left is not None and node.right is not None:
            temp_max = node.val + rightSonMax + leftSonMax
            self.max = temp_max if temp_max > self.max else self.max
            sonMax = leftSonMax if rightSonMax < leftSonMax else rightSonMax
            temp = sonMax + node.val
            return temp if temp >= 0 else 0

        elif node.left is not None:
            temp_max = node.val + leftSonMax
            self.max = temp_max if temp_max > self.max else self.max
            temp = leftSonMax + node.val
            return temp if temp >= 0 else 0

        elif node.right is not None:
            temp_max = node.val + rightSonMax
            self.max = temp_max if temp_max > self.max else self.max
            temp = rightSonMax + node.val
            return temp if temp >= 0 else 0

        else:
            print(node.val)
            self.max = node.val if node.val > self.max else self.max
            return node.val if node.val >= 0 else 0

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

            ret = Solution().maxPathSum(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()