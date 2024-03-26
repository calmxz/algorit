class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def reverse_doubly_linked_list(head):
    current = head

    # Traverse to the end of the list to find the new head
    while current.next:
        current = current.next

    # Swap prev and next pointers iteratively
    while current:
        current.next, current.prev = current.prev, current.next
        if current.prev is None:  # Reached the original head, so update new head
            head = current
        current = current.next

    return head

# Function to display the doubly linked list
def display_doubly_linked_list(head):
    current = head
    while current:
        print(current.data, end=" <-> " if current.next else " <-> None\n")
        current = current.next

# Create example doubly linked lists
example1_head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

example1_head.next = node2
node2.prev = example1_head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

example2_head = Node(10)
node20 = Node(20)
node30 = Node(30)

example2_head.next = node20
node20.prev = example2_head
node20.next = node30
node30.prev = node20

example3_head = Node(5)
node12 = Node(12)
node7 = Node(7)
node9 = Node(9)
node13 = Node(13)

example3_head.next = node12
node12.prev = example3_head
node12.next = node7
node7.prev = node12
node7.next = node9
node9.prev = node7
node9.next = node13
node13.prev = node9

# Display original doubly linked lists
print("Original Doubly Linked Lists:")
print("Example 1:")
display_doubly_linked_list(example1_head)
print("\nExample 2:")
display_doubly_linked_list(example2_head)
print("\nExample 3:")
display_doubly_linked_list(example3_head)

# Reverse the doubly linked lists
reversed_example1_head = reverse_doubly_linked_list(example1_head)
reversed_example2_head = reverse_doubly_linked_list(example2_head)
reversed_example3_head = reverse_doubly_linked_list(example3_head)

# Display reversed doubly linked lists
print("\nReversed Doubly Linked Lists:")
print("Example 1:")
display_doubly_linked_list(reversed_example1_head)
print("\nExample 2:")
display_doubly_linked_list(reversed_example2_head)
print("\nExample 3:")
display_doubly_linked_list(reversed_example3_head)
