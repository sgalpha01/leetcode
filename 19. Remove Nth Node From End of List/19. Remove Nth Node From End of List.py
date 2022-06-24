class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    r_node = head
    for _ in range(n):
        r_node = r_node.next

    if r_node is None:
        return head.next

    l_node = head
    while r_node.next:
        l_node = l_node.next
        r_node = r_node.next

    l_node.next = l_node.next.next
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


def arr_from_LL(head):
    if not head:
        return []
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


head = ll_from_arr([1, 2, 3, 4, 5])
removeNthFromEnd(head, 5)
print(arr_from_LL(removeNthFromEnd(head, 5)))