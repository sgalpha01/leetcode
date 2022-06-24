class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if left == right:
        return head

    dummy = ListNode()
    dummy.next = head
    prev, curr = dummy, dummy.next
    pos = 1

    while curr:
        if pos == left:
            left_node = curr
            curr = curr.next
            pos += 1
            break

        pos += 1
        prev, curr = curr, curr.next

    left_prev, prev = prev, left_node

    while curr:
        next = curr.next
        curr.next = prev

        if pos >= right:
            left_prev.next = curr
            left_node.next = next
            break

        pos += 1
        prev, curr = curr, next

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


ll = ll_from_arr(list(range(0)))
print(arr_from_ll(reverseBetween(ll, 0, 0)))
