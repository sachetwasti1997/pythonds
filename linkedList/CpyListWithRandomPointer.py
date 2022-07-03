from collections import deque
from typing import Optional
class Node:
    def __init__(self, x: int, nxt: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = nxt
        self.random = random

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    head_new = head
    while head_new:
        temp = Node(head_new.val)
        nxt = head_new.next
        head_new.next = temp
        temp.next = nxt
        head_new = head_new.next.next
    head_new = head
    new_head = head_new.next
    while head_new:
        if head_new.random and head_new.next:
            head_new.next.random = head_new.random.next
        head_new = head_new.next.next
    head_new = head
    while head_new.next:
        temp = head_new.next
        head_new.next = head_new.next.next
        head_new = temp
    return new_head


if __name__ == '__main__':
    l1 = Node(7)
    l2 = Node(13)
    l3 = Node(11)
    l4 = Node(10)
    l5 = Node(1)
    l1.next = l2
    l2.next = l3
    l2.random = l1
    l3.next = l4
    l4.next = l5
    l4.random = l3
    l5.random = l1
    newhead = copyRandomList(l1)
    while newhead:
        print(newhead == l1)
        newhead = newhead.next
        l1 = l1.next
    print(newhead)
