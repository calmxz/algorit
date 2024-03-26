from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_binary_tree():
    root_data = input("Enter data for root node: ")
    root = TreeNode(root_data)
    nodes_queue = deque([root])

    while nodes_queue:
        current_node = nodes_queue.popleft()
        left_data = input(f"Enter left child data for node {current_node.data} (press Enter if none, type 'done' to finish): ")
        if left_data.lower() == 'done':
            break
        elif left_data:
            current_node.left = TreeNode(left_data)
            nodes_queue.append(current_node.left)

        right_data = input(f"Enter right child data for node {current_node.data} (press Enter if none, type 'done' to finish): ")
        if right_data.lower() == 'done':
            break
        elif right_data:
            current_node.right = TreeNode(right_data)
            nodes_queue.append(current_node.right)

    return root

def display_binary_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print(" " * (level * 4) + prefix + "->", root.data)
        if root.left:
            display_binary_tree(root.left, level + 1, "L:")
        if root.right:
            display_binary_tree(root.right, level + 1, "R:")

def find_largest_in_levels(root):
    if root is None:
        return []

    max_values = []
    current_level = deque([root])

    while current_level:
        max_in_level = float('-inf')
        next_level = deque()

        for node in current_level:
            max_in_level = max(max_in_level, int(node.data))

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        max_values.append(max_in_level)
        current_level = next_level

    return max_values

# Main program
if __name__ == "__main__":
    print("Constructing Binary Tree:")
    binary_tree = construct_binary_tree()
    print("\nBinary Tree Structure:")
    display_binary_tree(binary_tree)

    largest_in_levels = find_largest_in_levels(binary_tree)
    print("\nLargest values in each level:")
    for i, value in enumerate(largest_in_levels):
        print(f"Level {i + 1}: {value}")