from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    prev, current, nxt = None, head, head.next

    while nxt:
        current.next = prev
        prev = current
        current = nxt
        nxt = nxt.next

    current.next = prev
    return current


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)

    l1.next = l2
    l2.next = l3
    l3.next = l4

    l1 = reverseList(l1)

    while l1:
        print(l1.val)
        l1 = l1.next
