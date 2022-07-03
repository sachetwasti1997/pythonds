from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt = None):
        self.val = val
        self.next = nxt

def hasCycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False
    curr, fast = head, head
    while fast and fast.next:
        if curr == fast:
            return True
        curr = curr.next
        fast = fast.next.next
    return False
