# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_right(head, k: int):
    length = 0
    node = head
    while node:
        end = node
        node = node.next
        length += 1

    k = k % length
    if k == 0:
        return head

    node = head
    for _ in range(length - k - 1):
        node = node.next

    dummy = ListNode()
    dummy.next = node.next
    node.next = None
    end.next = head

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


list1 = ll_from_arr([1, 2, 3, 4, 5])
print(arr_from_ll(rotate_right(list1, 5)))
