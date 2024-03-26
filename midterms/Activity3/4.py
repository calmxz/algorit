class TreeNode:
    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None

def construct_binary_tree():
    root_data = input("Enter data for root node: ")
    root = TreeNode(root_data)
    nodes_queue = [root]

    while nodes_queue:
        current_node = nodes_queue.pop(0)
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

def verify_children_sum_property(root):
    if root is None:
        return True

    # Get values of left and right children, treating None as 0
    left_value = root.left.data if root.left else 0
    right_value = root.right.data if root.right else 0

    # Check if the node's value matches the sum of its children's values
    if root.data == left_value + right_value:
        return True
    else:
        return False

# Main program
if __name__ == "__main__":
    print("Constructing Binary Tree:")
    binary_tree = construct_binary_tree()
    print("\nBinary Tree Structure:")
    display_binary_tree(binary_tree)

    # Verify if the children sum property is satisfied
    if verify_children_sum_property(binary_tree):
        print("\nChildren sum property is satisfied for the given binary tree.")
    else:
        print("\nChildren sum property is not satisfied for the given binary tree.")