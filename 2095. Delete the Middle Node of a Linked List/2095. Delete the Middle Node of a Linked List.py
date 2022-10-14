# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def delete_middle(head):
    if not head.next:
        return None
    slow = head
    fast = head
    while fast.next and fast.next.next and fast.next.next.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head


ll = ll_from_arr([1])
print(arr_from_ll(delete_middle(ll)))
