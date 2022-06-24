class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def del_duplis(head):
    dummy = pre = ListNode()
    dummy.next = head
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next
            head = head.next
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


list1 = ll_from_arr([1, 3, 3, 4, 4, 5, 6])
print(arr_from_ll(del_duplis(list1)))
