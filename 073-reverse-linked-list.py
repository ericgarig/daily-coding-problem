"""
Daily Coding Problem - 2018-12-20.

Given the head of a singly linked list, reverse it in-place.
"""


class Node(object):
    """Node object for a linked list."""

    def __init__(self, data=None, next=None):
        """Init."""
        self.data = data
        self.next = next


class LList():
    """Singly-linked list."""

    def __init__(self, head=None):
        """Init."""
        self.head = head
        self.size = 0

    def get_size(self):
        """Get the size of the linked list."""
        return self.size

    def add_node(self, data):
        """Add a node."""
        new_node = Node(data)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        self.size += 1

    def print_nodes(self):
        """Print all the nodes."""
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        """Given the head of a singly-linked list, reverse it inplace."""
        previous = None
        current = self.head
        while current is not None:
            original_next = current.next
            current.next = previous
            previous = current
            current = original_next
        self.head = previous
        return True


ll = LList()
ll.add_node(2)
ll.add_node(4)
ll.add_node(5)
ll.add_node(8)
ll.print_nodes()

print('reversing')
ll.reverse_list()
print('done')
ll.print_nodes()
