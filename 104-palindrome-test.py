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
        self.prev = prev
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
            curr = curr.getNextNode()

    def is_palindrome(self):
        """Determine if the list is a palindrome."""
        midpoint = self.size // 2
        current = self.head
        node_iter = 0
        list_stack = []
        while current is not None:
            if node_iter < midpoint:
                list_stack.append(current.data)
            elif node_iter == midpoint and self.size % 2 == 1:
                pass
            elif current.data != list_stack.pop():
                return False
            current = current.next
            node_iter += 1
        return True


class DoubleList(object):
    """Doubly-Linked list class."""

    head = None
    tail = None

    def append(self, data):
        """Add a new node object to the end of the list."""
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        """Remove the specified node value."""
        current_node = self.head

        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the
                    # next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None

            current_node = current_node.next

    def show(self):
        """Display the contents of the list."""
        print ('Show list data:', '-' * 34)
        cur = self.head
        while cur is not None:
            prev_val = cur.prev.data if hasattr(cur.prev, 'data') else None
            next_val = cur.next.data if hasattr(cur.next, 'data') else None
            print (prev_val, cur.data, next_val)

            cur = cur.next
        print ('-' * 50)

    def is_palindrome(self):
        """Determine if the list is a palindrome."""
        front = self.head
        end = self.tail
        while front is not None:
            if front.data != end.data:
                return False
            if front == end or front.next == end:
                return True
            front = front.next
            end = end.prev
        return True


d1 = DoubleList()
d1.append(1)
d1.append(4)
d1.append(3)
d1.append(4)
d1.append(1)
print(d1.is_palindrome(), 'DList, odd, matched')


d2 = DoubleList()
d2.append(1)
d2.append(4)
d2.append(3)
d2.append(5)
d2.append(1)
print(d2.is_palindrome(), 'DList, odd, unmatched')


d3 = DoubleList()
d3.append(1)
d3.append(4)
print(d3.is_palindrome(), 'DList, even, unmatched')


d4 = DoubleList()
d4.append(1)
d4.append(4)
d4.append(4)
d4.append(1)
print(d4.is_palindrome(), 'DList, even, matched')

s1 = LinkedList()
s1.append(1)
s1.append(2)
s1.append(1)
print(s1.is_palindrome(), 'SList, odd, matched')

s2 = LinkedList()
s2.append(1)
s2.append(2)
s2.append(3)
print(s2.is_palindrome(), 'SList, odd, unmatched')

s3 = LinkedList()
s3.append(1)
s3.append(2)
s3.append(3)
s3.append(1)
print(s3.is_palindrome(), 'SList, even, unmatched')

s4 = LinkedList()
s4.append(1)
s4.append(2)
s4.append(2)
s4.append(1)
print(s4.is_palindrome(), 'SList, even, matched')
