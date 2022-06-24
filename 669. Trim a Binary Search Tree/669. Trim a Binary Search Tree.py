from collections import deque


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


# Function to Build Tree
def build_tree(nodes):
    if nodes is None or nodes[0] is None:
        return None

    # Create the root of the tree
    root = TreeNode(int(nodes[0]))
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
            curr_node.left = TreeNode(int(curr_val))

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
            curr_node.right = TreeNode(int(curr_val))

            # Push it to the queue
            q.append(curr_node.right)
            size += 1
        i += 1
    return root


def trim_bst(root, low: int, high: int):
    def dfs(node, parent):
        if not node:
            return
        if node.val < low:
            parent.left = node.right
            dfs(node.right, parent)
        elif node.val > high:
            parent.right = node.left
            dfs(node.left, parent)
        else:
            dfs(node.left, node)
            dfs(node.right, node)

    dummy = TreeNode()
    dummy.left = root
    dfs(root, dummy)
    return dummy.left if dummy.left and low <= dummy.left.val <= high else dummy.right


null = None
tree = build_tree([3])
trim_bst(tree, 2, 2)
