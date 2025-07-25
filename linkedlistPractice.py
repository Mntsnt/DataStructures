
# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # store data
        self.next = None  # pointer to next node 

# Define LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # initially empty list

    # Method to insert at end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to display the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)

llist.display()
