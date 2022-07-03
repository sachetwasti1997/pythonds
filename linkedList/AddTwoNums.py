from typing import Optional

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    newhead = ListNode()
    tail = newhead
    carry = 0

    while l1 is not None or l2 is not None:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry
        carry = total // 10
        tail.next = ListNode(total % 10)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        tail = tail.next

    if carry > 0:
        tail.next = ListNode(carry)

    return newhead.next
