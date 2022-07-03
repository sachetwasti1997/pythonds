from typing import Optional

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def reorderList(head: Optional[ListNode]) -> None:
    if not head.next:
        return head

    def reverse(start) -> ListNode:
        if not start.next:
            return start
        prev, current, nxt = None, start, start.next
        while nxt:
            current.next = prev
            prev = current
            current = nxt
            nxt = nxt.next
        current.next = prev
        return current

    first = None
    slow = head
    fast = head

    while fast and fast.next:
        first = slow
        slow = slow.next
        fast = fast.next.next

    first.next = None
    slow = reverse(slow)
    l1 = head
    tail = l1
    l1 = l1.next
    isHead = False
    while l1 and slow:
        if isHead:
            tail.next = l1
            l1 = l1.next
            isHead = False
        else:
            tail.next = slow
            slow = slow.next
            isHead = True
        tail = tail.next

    if l1:
        tail.next = l1
    elif slow:
        tail.next = slow

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    print(reorderList(l1))
    while l1:
        print(l1.val)
        l1 = l1.next
