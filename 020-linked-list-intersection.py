"""
Daily Coding Problem - 2018-10-27.

Given two singly linked lists that intersect at some point, find the
intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same value are the exact same
node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists)
and constant space.
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


def find_intersection(llist_a, llist_b):
    """Given two singly-linked lists, find the intersecting node."""
    size = llist_a.size
    llist_a = llist_a.head
    llist_b = llist_b.head
    for i in range(size):
        if llist_a.data == llist_b.data:
            return llist_a.data
        llist_a = llist_a.next
        llist_b = llist_b.next
    return None


llist_a = LList()
llist_a.add_node(3)
llist_a.add_node(7)
llist_a.add_node(8)
llist_a.add_node(10)

llist_b = LList()
llist_b.add_node(99)
llist_b.add_node(1)
llist_b.add_node(8)
llist_b.add_node(3)

print(find_intersection(llist_a, llist_b))    # 8
