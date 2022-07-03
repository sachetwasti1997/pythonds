from typing import Optional

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    count = 0
    new_head = head
    while new_head:
        new_head = new_head.next
        count += 1

    if count == n:
        return head.next

    prev, current = None, head

    for i in range(n):
        current = current.next

    while current:
        if prev is None:
            prev = head
        else:
            prev = prev.next
        current = current.next

    prev.next = prev.next.next
    return head
