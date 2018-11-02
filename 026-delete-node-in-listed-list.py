"""
Daily Coding Problem - 2018-11-02.

Given a singly linked list and an integer k, remove the kth last element
from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class Node(object):
    """Node object that knows it's value and points to next element."""

    def __init__(self, data=None):
        """Init."""
        self.data = data
        self.next = None


class SLinkedList(object):
    """Singly linked list."""

    def __init__(self):
        """Init."""
        self.head = None

    def add_element(self, new_data):
        """Add a new element at the end of the linked list."""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_element = self.head
        while(last_element.next):
            last_element = last_element.next
        last_element.next = new_node

    def listprint(self):
        """Print the list."""
        val = self.head
        while val is not None:
            print (val.data)
            val = val.next
        print ('---')

    def remove_pos(self, k):
        """Remove the k-th element in the linked list."""
        val = self.head
        for _ in range(k - 2):
            val = val.next
        val.next = val.next.next


list1 = SLinkedList()
list1.add_element("Mon")
list1.add_element("Tue")
list1.add_element("Wed")
list1.add_element("Thu")
list1.add_element("Fri")
list1.add_element("Sat")

list1.listprint()
list1.remove_pos(2)
list1.listprint()
