"""
https://blog.csdn.net/Whyalwaysxu/article/details/90919321
"""
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
            nodes = [root]
            while nodes:
                temp = []
                for node in nodes:
                    if node:
                        ret.append(node.val)
                        temp += [node.left, node.right]
                    else:
                        ret.append(None)
                if temp.count(None) == len(temp):
                    break
                nodes = temp
        return ",".join(map(str, ret))



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data:
            nodes = [TreeNode(int(i)) if i != 'None' else None for i in data.split(',')]
            print(nodes)
            n = len(nodes)
            end = 1
            start = 0
            while True:
                if end >= n:
                    break
                nextLevel = end
                for node in nodes[start:end]:
                    if node:
                        node.left = nodes[nextLevel]
                        node.right = nodes[nextLevel+1]
                        nextLevel += 2
                start = end
                end = nextLevel
            return nodes[0]
        return None


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

node1 = TreeNode(-1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node1.right = node3
node1.left = node2
# node3.left = node4
# node3.right = node5
# node4.left = node6
# node5.left = node7
# node5.right = node8
codec = Codec()
print(codec.serialize(node1))
print(codec.deserialize(codec.serialize(node1)).val)
