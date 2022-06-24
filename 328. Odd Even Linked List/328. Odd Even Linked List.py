def odd_even_list(head):
    if head is None:
        return None

    head_2 = head.next
    odd, even = head, head.next

    while even and even.next:
        next_2 = even.next
        next_3 = next_2.next
        odd.next = next_2
        even.next = next_3
        odd = next_2
        even = next_3

    odd.next = head_2
    return head


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


ll = ll_from_arr([1])
print(arr_from_ll(odd_even_list(ll)))
