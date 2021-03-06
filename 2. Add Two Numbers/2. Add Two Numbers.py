class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    carry = 0
    root = n = ListNode(0)

    while l1 or l2 or carry:
        v1 = v2 = 0

        if l1:
            v1 = l1.val
            l1 = l1.next

        if l2:
            v2 = l2.val
            l2 = l2.next

        carry, val = divmod(v1 + v2 + carry, 10)
        n.next = ListNode(val)
        n = n.next

    return root.next


l1 = ListNode(9)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
# l2.next.next = ListNode(4)


def traverse_ll(head):
    if head is None:
        return

    while head:
        print(head.val, end=" ")
        head = head.next


traverse_ll(addTwoNumbers(l1, l2))
