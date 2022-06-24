class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: list) -> ListNode:
    from heapq import heapify, heappop, heapreplace

    heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    heapify(heap)
    curr = dummy = ListNode()
    while heap:
        _, i, node = heap[0]
        if not node.next:
            heappop(heap)
        else:
            heapreplace(heap, (node.next.val, i, node.next))

        curr.next = node
        curr = curr.next

    return dummy.next
