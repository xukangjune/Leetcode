"""
使用双向链表和哈希表。首先，字典键是key，然后值是节点node。node构成节点的双向链表。可以根据node很快的进行删除，每次更新时，先删除，然后将node置于
链表前部（其中head和tail永远是头和尾）。
"""
class LinkList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.post = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.keys = []
        self.cache = dict()
        self.head = self.tail = LinkList(0, 0)
        self.head.post = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.adoptList(self.cache[key]).value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:   #已经在缓存内部，进行重写
            self.adoptList(self.cache[key]).value = value
        else:
            node = LinkList(key, value)
            self.cache[key] = node
            self.head.post.prev = node
            node.post = self.head.post
            node.prev = self.head
            self.head.post = node
            self.count += 1
            if self.count > self.capacity:
                node = self.tail.prev
                del self.cache[node.key]
                node.prev.post = node.post
                node.post.prev = node.prev

    def adoptList(self, node):
        node.prev.post = node.post
        node.post.prev = node.prev
        self.head.post.prev = node
        node.post = self.head.post
        node.prev = self.head
        self.head.post = node
        return node


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))


