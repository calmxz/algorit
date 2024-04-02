class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def in_order_traversal(root):
    result = []
    if root:
        result.extend(in_order_traversal(root.left))
        result.append(root.val)
        result.extend(in_order_traversal(root.right))
    return result

def pre_order_traversal(root):
    result = []
    if root:
        result.append(root.val)
        result.extend(pre_order_traversal(root.left))
        result.extend(pre_order_traversal(root.right))
    return result

def post_order_traversal(root):
    result = []
    if root:
        result.extend(post_order_traversal(root.left))
        result.extend(post_order_traversal(root.right))
        result.append(root.val)
    return result

def max_depth(root):
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1

def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    if not root:
        return True

    return is_mirror(root.left, root.right)

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

    print("\nIn-order Traversal:")
    result_in_order = in_order_traversal(root)
    print(result_in_order)

    print("\nPre-order Traversal:")
    result_pre_order = pre_order_traversal(root)
    print(result_pre_order)

    print("\nPost-order Traversal:")
    result_post_order = post_order_traversal(root)
    print(result_post_order)

    print("\nMaximum Depth of Binary Tree:")
    max_depth_val = max_depth(root)
    print(max_depth_val)

    print("\nSymmetric Tree:")
    symmetric = is_symmetric(root)
    print(symmetric)

if __name__ == "__main__":
    main()