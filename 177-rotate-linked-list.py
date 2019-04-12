u"""
Daily Coding Problem - 2019-01-20.

Determine whether a doubly linked list is a palindrome. What if it’s
singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""


class Node(object):
    """Node class."""

    def __init__(self, data, prev, next):
        """Init."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Singly-Linked list class."""

    def __init__(self, head=None):
        """Init."""
        self.head = head
        self.size = 0

    def get_size(self):
        """Get size of linked list."""
        return self.size

    def append(self, data):
        """Add new node."""
        new_node = Node(data, None, None)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        self.size += 1

    def show(self):
        """Display contents of list."""
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def rotate(self, k):
        """Rotate the specified linked list by k values."""
        k = k % self.size
        k -= 1
        current = self.head
        for i in range(self.size):
            if i + 1 != self.size:
                current = current.next
            if i == k:
                new_head = current
            if i + 1 == k:
                tail = current
        current.next = self.head
        tail.next = None
        self.head = new_head


s1 = LinkedList()
s1.append(1)
s1.append(2)
s1.append(3)
s1.append(4)
s1.append(5)

s1.show()
s1.rotate(2)
print("-- rotated --")
s1.show()
