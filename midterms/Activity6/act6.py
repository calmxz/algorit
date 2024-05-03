class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # Traversal
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node, depth=0):
        if node:
            print("  " * depth + str(node.key))
            self.preorder_traversal(node.left, depth + 1)
            self.preorder_traversal(node.right, depth + 1)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=" ")

    # Deletion
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return None  # Node to delete found, return None to delete it

        node.left = self._delete_recursive(node.left, key)
        node.right = self._delete_recursive(node.right, key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def display(self):
        self._display_recursively(self.root, 0)

    def _display_recursively(self, root, level):
        if root:
            self._display_recursively(root.right, level + 1)
            print("   " * level + str(root.key))
            self._display_recursively(root.left, level + 1)

# Menu for CRUD operations
def main():
    tree = BinaryTree()
    while True:
        print("\nBinary Tree Operations:")
        print("1. Insert")
        print("2. Inorder Traversal")
        print("3. Preorder Traversal")
        print("4. Postorder Traversal")
        print("5. Delete")
        print("6. Visualize")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = int(input("Enter key to insert: "))
            tree.insert(key)
            print("Node inserted successfully.")
        elif choice == "2":
            print("Inorder Traversal:")
            tree.inorder_traversal(tree.root)
        elif choice == "3":
            print("Preorder Traversal:")
            tree.preorder_traversal(tree.root)
        elif choice == "4":
            print("Postorder Traversal:")
            tree.postorder_traversal(tree.root)
        elif choice == "5":
            key = int(input("Enter key to delete: "))
            if tree.root is None:
                print("Tree is empty. Nothing to delete.")
            else:
                tree.root = tree._delete_recursive(tree.root, key)
                print("Node deleted successfully.")
        elif choice == "6":
            print("Tree Visualization:")
            tree.display()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()