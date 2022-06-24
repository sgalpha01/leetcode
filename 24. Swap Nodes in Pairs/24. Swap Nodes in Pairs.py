# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    prev = dummy = ListNode()
    prev.next = head

    while prev.next and prev.next.next:
        a = prev.next
        b = a.next
        prev.next, b.next, a.next = b, a, b.next

        prev = a

    return dummy.next


def ll_from_arr(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next

    return head


def arr_from_ll(head):
    if not head:
        return []
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


ll = ll_from_arr([1, 2, 3, 4, 5])
print(arr_from_ll(swapPairs(ll)))
