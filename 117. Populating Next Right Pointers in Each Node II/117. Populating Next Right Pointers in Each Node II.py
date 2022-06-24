from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


# Function to Build Tree
def build_tree(nodes):
    if nodes is None or nodes[0] is None:
        return None

    # Create the root of the tree
    root = Node(int(nodes[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size += 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(nodes):
        # Get and remove the front of the queue
        curr_node = q[0]
        q.popleft()
        size -= 1

        # Get the current node's value from the string
        curr_val = nodes[i]

        # If the left child is not null
        if curr_val is not None:

            # Create the left child for the current node
            curr_node.left = Node(int(curr_val))

            # Push it to the queue
            q.append(curr_node.left)
            size += 1
        # For the right child
        i += 1
        if i >= len(nodes):
            break
        curr_val = nodes[i]

        # If the right child is not null
        if curr_val is not None:

            # Create the right child for the current node
            curr_node.right = Node(int(curr_val))

            # Push it to the queue
            q.append(curr_node.right)
            size += 1
        i += 1
    return root


def connect(root):
    if not root:
        return
    stack = deque([root])
    while stack:
        n = len(stack)
        for i in range(n):
            node = stack.popleft()
            node.next = stack[0] if i < n - 1 else None
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return root


null = None

root = build_tree([1, 2, 3, 4, 5, null, 7])
print(connect(root))
