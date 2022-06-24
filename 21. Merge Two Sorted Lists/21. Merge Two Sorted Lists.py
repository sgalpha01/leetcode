class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = curr = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next

        curr = curr.next

    curr.next = l1 or l2
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


h1 = ll_from_arr([1, 3, 5, 7])
h2 = ll_from_arr([0, 2, 4, 6, 8])

ans = mergeTwoLists(h1, h2)
print(arr_from_ll(ans))
print(arr_from_ll(h1))
print(arr_from_ll(h2))
