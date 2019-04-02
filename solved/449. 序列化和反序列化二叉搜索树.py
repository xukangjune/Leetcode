"""
第一部分是我自己写的，用了类属性来记录状态，不知道可不可以。
第二种方法是看别人写的，非常有用。其实由于第一个函数serialize不会检查输出是什么，所以这里用数组代替。也是使用递归函数，
每次检查这一层的节点，如果是空，就返回None。如果不是空，但是没有子节点，返回该节点的数组（长度为1）。剩余的情况就是返回
含有子节点的节点。长度为3，第一个就是该节点的值，第二个是该节点递归左节点返回的数组（没有子节点就是[])；同样，第三个是
递归右节点的数组（没有就是空）。最后一起返回到上层函数。
反序列化时，传入数组。先检查数组的长度，如果为空，说明返回None。如果为1，说明没有子节点，所以不用使用递归函数。接下来
就是长度为3情况，假如左节点不为空，递归它，右节点不为空，办他。最后返回这个节点到上层函数。
"""
from tree_traversal import postorderTrav
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if root is None:
            return []

        elif root.left is None and root.right is None:
            return [root.val]

        elif root.left and root.right is None:
            return [root.val, self.serialize(root.left), []]

        elif root.right and root.left is None:
            return [root.val, [], self.serialize(root.right)]

        else:
            return [root.val,self.serialize(root.left), self.serialize(root.right)]

        # def serializeCore(node):
        #     if node:
        #         self.data += node.val
        #         self.data += ','
        #         serializeCore(node.left)
        #         serializeCore(node.right)
        #     else:
        #         self.data += '$'
        #         self.data += ','
        #
        # self.data = ""
        # serializeCore(root)
        # return self.data


    def deserialize(self, data):
        if not data:
            return None

        elif len(data) == 1:
            return TreeNode(data[0])

        else:
            root = TreeNode(data[0])
            if data[1]:
                root.left = self.deserialize(data[1])
            if data[2]:
                root.right = self.deserialize(data[2])
            return root

        # temp = data.split(",")
        # length = len(temp)
        # def deserializeCore():
        #     if self.i >=length or temp[self.i] == '$':
        #         return None
        #     else:
        #         node = TreeNode(temp[self.i])
        #         self.i += 1
        #         node.left = deserializeCore()
        #         self.i += 1
        #         node.right = deserializeCore()
        #         return node
        #
        # self.i = 0
        # return deserializeCore()

solve = Codec()
data = '1,2,$,$,3'
a = solve.serialize(data)
print(a)
ret = solve.deserialize(a)
print(ret.val)