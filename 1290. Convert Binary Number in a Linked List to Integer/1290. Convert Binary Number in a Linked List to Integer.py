def get_decimal(head):
    res = 0
    while head:
        res = (res << 1) | head.val
        head = head.next

    return res
