class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key
        
def printInorder(root):
    if root:
        print(root.val, end = " ")
        printInorder(root.left)
        printInorder(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    printInorder(root)    