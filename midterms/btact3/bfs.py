from collections import defaultdict, deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None  # Pointer to the next node at the same level

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.extend(level)

    return result

def min_depth(root):
    if not root:
        return 0

    queue = [(root, 1)]

    while queue:
        node, depth = queue.pop(0)

        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))

        if node.right:
            queue.append((node.right, depth + 1))

def max_width(root):
    if not root:
        return 0

    max_width = 0
    queue = [(root, 1)]

    while queue:
        level_size = len(queue)
        max_width = max(max_width, level_size)

        for _ in range(level_size):
            node, position = queue.pop(0)

            if node.left:
                queue.append((node.left, 2 * position))

            if node.right:
                queue.append((node.right, 2 * position + 1))

    return max_width

def connect_nodes_at_same_level(root):
    if not root:
        return

    # Queue for level order traversal
    queue = [root]

    while queue:
        level_size = len(queue)
        prev = None  # Pointer to the previous node at the same level

        for _ in range(level_size):
            current = queue.pop(0)

            # Connect the current node to the previous node
            if prev:
                prev.next = current

            prev = current

            # Add children of the current node to the queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

def vertical_order_traversal(root):
    if not root:
        return []

    # Dictionary to store nodes at each vertical level
    vertical_levels = defaultdict(list)
    min_hd = float('inf')
    max_hd = float('-inf')

    # Queue for BFS traversal
    queue = deque([(root, 0)])  # Tuple: (node, horizontal distance)

    while queue:
        node, hd = queue.popleft()

        # Update min and max horizontal distances
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        # Store the node at the current horizontal distance level
        vertical_levels[hd].append(node.val)

        # Enqueue left and right children with updated horizontal distances
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Collect nodes at each vertical level
    result = []
    for i in range(min_hd, max_hd + 1):
        result.extend(vertical_levels[i])

    return result

def main():
    root_val = int(input("Enter the value of the root node: "))
    root = TreeNode(root_val)
    nodes = [(root, "root")]

    while nodes:
        current, node_type = nodes.pop(0)
        left_val = input(f"Enter the value of the left child of {current.val} (or type 'None' if no left child): ")
        if left_val.lower() != 'none':
            left_child = TreeNode(int(left_val))
            current.left = left_child
            nodes.append((left_child, "left child of " + str(current.val)))

        right_val = input(f"Enter the value of the right child of {current.val} (or type 'None' if no right child): ")
        if right_val.lower() != 'none':
            right_child = TreeNode(int(right_val))
            current.right = right_child
            nodes.append((right_child, "right child of " + str(current.val)))

    print("\nLevel Order Traversal (BFS):")
    result = level_order_traversal(root)
    print(result)

    print("\nMinimum Depth of Binary Tree:")
    min_depth_val = min_depth(root)
    print(min_depth_val)

    print("\nMaximum Width of Binary Tree:")
    max_width_val = max_width(root)
    print(max_width_val)

    print("\nConnect Nodes at Same Level:")
    connect_nodes_at_same_level(root)
    current = root
    while current:
        print(f"Node {current.val} points to {current.next.val if current.next else 'None'} at the same level")
        current = current.left

    print("\nVertical Order Traversal:")
    result = vertical_order_traversal(root)
    print(result)

if __name__ == "__main__":
    main()