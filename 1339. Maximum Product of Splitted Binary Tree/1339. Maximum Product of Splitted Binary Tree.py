from collections import deque


class TreeNode:
    def __init__(self, val):
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


tree = build_tree([1, 2, 3, 4, 5, 6])


def max_product(root):
    MOD = 10**9 + 7
    total_sum = tree_sum(root)
    res = 1

    def dfs(root):
        nonlocal res
        if not root:
            return
        res = max(res, (total_sum - root.val) * root.val)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return res % MOD


def tree_sum(root):
    if not root:
        return 0
    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)
    curr_sum = root.val + left_sum + right_sum
    root.val = curr_sum
    return curr_sum


print(max_product(tree))
