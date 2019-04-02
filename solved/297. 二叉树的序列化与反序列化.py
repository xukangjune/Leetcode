# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []
        if root:
            queue = [root]
            while queue:
                node = queue[0]
                if node:
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append(None)
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append(None)
                    ret.append(node.val)
                else:
                    ret.append(None)
                del queue[0]
            while not ret[-1]:
                ret.pop()
        return str(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.lstrip('[').rstrip(']').split(',')
        print(data)
        n = len(data)
        print(n)
        if not data[0]:
            return
        for i in range(n):
            data[i] = int(data[i]) if data[i][-1].isdigit() else None
        print(data)
        data[0] = TreeNode(data[0])
        level = [0]
        j = 0
        while level:
            temp = []
            if level[0] + 2 * len(level) < n:
                temp = [level[0] + i for i in range(1, 2 * len(level) + 1)]
            else:
                temp = [i for i in range(level[-1]+1, n)]
            j = 0
            while j < 2 * len(level):
                for i in level:
                    if data[i]:
                        data[i].left = None if data[temp[j]] is None else TreeNode(data[temp[j]])
                        j += 1
                        data[i].right = None if data[temp[j]] is None else TreeNode(data[temp[j]])
                        j += 1








# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


solve = Codec()
node3 = TreeNode(3)
node4 = TreeNode(4)
node2 = TreeNode(2)
node2.left = node3
node2.right = node4
node6 = TreeNode(6)
node5 = TreeNode(5)
node5.right = node6
node1 = TreeNode(1)
node1.left = node2
node1.right = node5
print(solve.serialize(node1))
print(solve.deserialize('[]'))
# print(solve.deserialize(solve.serialize(node1)).val)