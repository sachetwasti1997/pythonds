import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class pairVal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        return self.first < other.first


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    h = []
    for i in lists:
        h.append(pairVal(i.val, i.next))
    heapq.heapify(h)
    l1, head = None, None
    while len(h) > 0:
        temp = heapq.heappop(h)
        if l1 is None:
            l1 = ListNode(temp.first)
            head = l1
        else:
            l1.next = ListNode(temp.first)
            l1 = l1.next
        if temp.second is not None:
            heapq.heappush(h, pairVal(temp.second.val, temp.second.next))

    return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l12 = ListNode(4)
    l13 = ListNode(5)

    l1.next = l12
    l12.next = l13

    l2 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)

    l2.next = l22
    l22.next = l23

    l3 = ListNode(2)
    l32 = ListNode(6)

    l3.next = l32

    res = mergeKLists([l1, l2, l3])
    while res:
        print(res.val)
        res = res.next
