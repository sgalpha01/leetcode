class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    if k <= 1:
        return head
    curr = dummy = ListNode()
    curr.next = head
    while True:
        i = 0
        kth_node = curr
        while kth_node and i < k + 1:
            kth_node = kth_node.next
            i += 1

        if i != k + 1:
            return dummy.next

        next, tail = reverse_ll(curr.next, k)
        curr.next = next
        tail.next = kth_node
        curr = tail


def reverse_ll(head, k):
    prev = None
    curr = tail = head

    i = 0

    while curr and i < k:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next
        i += 1

    return prev, tail


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


ll = ll_from_arr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr_from_ll(reverseKGroup(ll, 3)))
