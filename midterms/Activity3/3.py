class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])

    return root

def display_binary_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print(" " * (level * 4) + prefix + "->", root.data)
        if root.left:
            display_binary_tree(root.left, level + 1, "L:")
        if root.right:
            display_binary_tree(root.right, level + 1, "R:")

# Main program
if __name__ == "__main__":
    input_array = input("Enter a sorted array of integers separated by spaces: ")
    sorted_array = sorted(map(int, input_array.split()))  # Sort the input array

    bst_root = sorted_array_to_bst(sorted_array)
    print("Binary Search Tree Constructed from Sorted Array:")
    display_binary_tree(bst_root)
