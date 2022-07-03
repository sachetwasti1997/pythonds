from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> Optional['Node']:
    if node is None: return None
    node_map = {}
    q = deque()
    q.append(node)
    while len(q):
        t = q.popleft()
        if t.val not in node_map:
            node_map[t.val] = Node(t.val)
        for i in t.neighbors:
            if i.val not in node_map:
                node_map[i.val] = Node(i.val)
                q.append(i)
            node_map[t.val].neighbors.append(node_map[i.val])
    return node_map[node.val]
