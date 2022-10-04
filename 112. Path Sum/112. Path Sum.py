from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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


def path_sum(root, target_sum):
    res = [False]

    def dfs(root, curr_sum):
        if root is None:
            return
        if (
            root.left is None
            and root.right is None
            and curr_sum + root.val == target_sum
        ):
            res[0] = True
            return
        dfs(root.left, curr_sum + root.val)
        dfs(root.right, curr_sum + root.val)

    dfs(root, 0)
    return res[0]


null = None
tree = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]
tree = build_tree(tree)
print(path_sum(tree, 22))
