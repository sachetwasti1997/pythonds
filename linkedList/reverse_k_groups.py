from typing import Optional

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if k == 1: return head
    l1 = head
    newHead, start, groupnext, count = None, None, None, 0
    while True:
        temp = k
        t = l1
        while temp > 0 and t:
            t = t.next
            temp -= 1
        if temp != 0:
            break
        prev, curr, nxt = t, l1, l1.next
        groupnext = curr
        while nxt != t:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        curr.next = prev
        if count >= 1: groupnext.next = curr
        if newHead is None: newHead = curr
        l1 = t
        count += 1

    return newHead

if __name__ == '__main__':
    head = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    head.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    res = reverseKGroup(head, 2)
    print(res)
    while res:
        print(res.val)
        res = res.next
