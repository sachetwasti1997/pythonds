from collections import deque
from typing import Optional
class Node:
    def __init__(self, x: int, nxt: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = nxt
        self.random = random

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    headnew = head
    while headnew:
        temp = Node(headnew.val)
        nxt = headnew.next
        headnew.next = temp
        temp.next = nxt
        headnew = headnew.next.next
    headnew = head
    newhead = headnew.next
    while headnew:
        if headnew.random and headnew.next: headnew.next.random = headnew.random.next
        headnew = headnew.next.next
    headnew = head
    while headnew.next:
        temp = headnew.next
        headnew.next = headnew.next.next
        headnew = temp
    return newhead


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
