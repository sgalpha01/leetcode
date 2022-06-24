def connect(root):
    node = root
    while node and node.left:
        next_level = node.left
        while node:
            node.left.next = node.right
            node.right.next = node.next and node.next.left
            node = node.next
        node = next_level

    return root
