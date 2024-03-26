import random

class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        
    def insert_at_end(self, new_data):
        new_node = Node(data=new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty. No node to delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_from_end(self):
        if self.head is None:
            print("List is empty. No node to delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def display_from_beginning(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_from_end(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# Generate 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Create a doubly linked list and insert the random numbers
dll = DoublyLinkedList()
for num in random_numbers:
    dll.insert_at_beginning(num)

# Display the doubly linked list
print("Doubly linked list after inserting 5 random numbers:")
dll.display_from_beginning()

# Main loop for user interaction
while True:
    print("\nChoose an action:")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete from beginning")
    print("4. Delete from end")
    print("5. Read from beginning")
    print("6. Read from end")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_data_beginning = int(input("Enter a number to insert at the beginning: "))
        dll.insert_at_beginning(new_data_beginning)
        print("Doubly linked list after insertion at the beginning:")
        dll.display_from_beginning()
    elif choice == "2":
        new_data_end = int(input("Enter a number to insert at the end: "))
        dll.insert_at_end(new_data_end)
        print("Doubly linked list after insertion at the end:")
        dll.display_from_beginning()
    elif choice == "3":
        dll.delete_from_beginning()
        print("Doubly linked list after deletion from the beginning:")
        dll.display_from_beginning()
    elif choice == "4":
        dll.delete_from_end()
        print("Doubly linked list after deletion from the end:")
        dll.display_from_beginning()
    elif choice == "5":
        print("Doubly linked list from the beginning:")
        dll.display_from_beginning()
    elif choice == "6":
        print("Doubly linked list from the end:")
        dll.display_from_end()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")