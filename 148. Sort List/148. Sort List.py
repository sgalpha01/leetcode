# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head):
    if head is None or head.next is None:
        return head

    mid = get_mid(head)
    left = sort_list(head)
    right = sort_list(mid)
    return merge(left, right)


def get_mid(head):
    fast = slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None
    return mid


def merge(head1, head2):
    dummy = tail = ListNode()
    while head1 and head2:
        if head1.val < head2.val:
            tail.next, head1 = head1, head1.next
        else:
            tail.next, head2 = head2, head2.next

        tail = tail.next

    tail.next = head1 or head2
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


ll = ll_from_arr([6, 5, 4, 3, 2, 1])
print(arr_from_ll(sort_list(ll)))
