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


def insertion_sort_ll(head):
    if head is None:
        return None

    dummy = ListNode(None)
    dummy.next = head
    prev = head
    node = head.next

    while node:
        if node.val < prev.val:
            start = dummy.next
            prev_2 = dummy

            while start.val < node.val:
                prev_2 = start
                start = start.next

            prev.next = node.next
            prev_2.next = node
            node.next = start
            node = prev.next

        else:
            prev = node
            node = node.next
        print(arr_from_ll(dummy.next))

    return dummy.next


ll = ll_from_arr([4, 2, 1, 3])
print(arr_from_ll(insertion_sort_ll(ll)))
