class Node:
    def __init__(self, key: int, val: int, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.map = {}

    def move_to_top(self, node: Node):
        if node is self.head:
            return
        if node is self.tail:
            self.tail = self.tail.prev
            node.prev.next = node.next
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.move_to_top(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self.move_to_top(self.map[key])
            return
        self.map[key] = Node(key, value)
        if self.head is None:
            self.head = self.map[key]
            self.tail = self.head
            self.count = 1
            return
        if self.capacity == 1:
            del self.map[self.head.key]
            self.head = self.map[key]
            self.tail = self.head
            self.count = 1
            return
        if self.capacity == self.count:
            self.count -= 1
            del self.map[self.tail.key]
            self.tail = self.tail.prev
            self.tail.next = None
        self.head.prev = self.map[key]
        self.map[key].next = self.head
        self.head = self.map[key]
        self.count += 1


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 0)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
