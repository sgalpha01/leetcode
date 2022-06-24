from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    stack = deque()

    while slow:
        stack.append(slow)
        slow = slow.next

    node = head

    while stack:
        temp = node.next
        node.next = stack.pop()
        node.next.next = temp
        node = temp

    node.next.next = None

    return head


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


ll = ll_from_arr([1, 2, 3, 4])
print(arr_from_ll(reorder_list(ll)))
