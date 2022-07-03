from typing import Optional

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    head, tail = None, None

    while l1 and l2:
        if l1.val < l2.val:
            maxNode = l1
            l1 = l1.next
        else:
            maxNode = l2
            l2 = l2.next
        if not head:
            head = ListNode(maxNode.val)
            tail = head
        else:
            tail.next = ListNode(maxNode.val)
            tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return head

if __name__ == '__main__':
    pass
