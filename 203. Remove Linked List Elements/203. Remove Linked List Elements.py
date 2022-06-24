def remove_elements(head, val):
    if head is None:
        return

    while head and head.val == val:
        head = head.next

    curr = head
    prev = head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr

        curr = curr.next

    return head
