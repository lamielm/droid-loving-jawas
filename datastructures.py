"Various Data Structures"

# Landon Lamie
# CIS 226
# 11/1/24

# System Imports
import os


class LinkedList:
    """Linked List Data Structure"""

    class Node:
        """Node in a data structure"""

        def __init__(self):
            """Constructor"""
            self.data = None
            self.next = None

    def __init__(self):
        """Constructor"""
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def is_empty(self):
        """Whether the linked list is empty or not"""
        return self._head is None

    @property
    def size(self):
        """Property for size"""
        return self._size

    def add_to_front(self, data):
        """Add a new element to the front of the linked list. Big O of O(1)"""
        # Make a new variable to also reference the head of the list
        old_head = self._head
        # Make a new node and assign it to the head variable
        self._head = self.Node()
        # Set the data on the new Node
        self._head.data = data
        # Make the next property of the Node point to the old head
        self._head.next = old_head
        # Increment the size of the list
        self._size += 1
        # Ensure that if we adding the very first node to the linked list
        # that the tail will be pointing to the new node we create
        if self._size == 1:
            self._tail = self._head

    def add_to_back(self, data):
        """Add a new element to the back of the linked list. Big O of O(1)"""
        # Make a pointer to the tail called old tail
        old_tail = self._tail
        # Make a new node and assign it to the tail variable
        self._tail = self.Node()
        # Assign the data and set the next pointer
        self._tail.data = data
        self._tail.next = None  # Not needed since constructor sets it. Shown for clarity.
        # Increment the size
        self._size += 1
        # Check to see if the list is empty. If so, make the head point to the
        # same location as the tail.
        if self._size == 1:
            self._head = self._tail
        else:
            old_tail.next = self._tail

    def remove_from_front(self):
        """Remove an element from the front of the linked list. Big O of O(1)"""
        # If the list is empty raise an error
        if self.is_empty:
            raise IndexError("Nothing to remove. List is empty.")

        # Let's get the data to return
        data = self._head.data
        # Move the head pointer to teh next in the list
        self._head = self._head.next
        # Decrease the size of the list.
        self._size -= 1
        # Check to see if we just removed the last node from the list.
        if self.is_empty:
            # If so, tail needs to be set to None
            self._tail = None

        # Return the dat from the removed node
        return data

    def remove_from_back(self):
        """Remove an element from the back of the linked list. Big O of O(N)"""
        # If the list is empty raise an error
        if self.is_empty:
            raise IndexError("Nothing to remove. List is empty.")

        # Get the data to return
        data = self._tail.data

        # Check to see if we are on the last node.
        # If so, we can just set the head and tail to None since we want
        # to remove the only remaining node in the list.
        if self._head == self._tail:
            self._head = None
            self._tail = None
        # Else, we need to traverse the list and stop right before we reach the tail.
        else:
            # Create a temporary node to use to "walk" down the list
            current = self._head
            # Keep moving forward until the current.next is equal to the tail.
            while current.next != self._tail:
                # Set the current pointer to the current pointer's next node
                current = current.next

            # We are now in a position to do some work.
            # Set the tail to the current position
            self._tail = current

            # Make the last node that we are removing go away
            # by setting tail's next property to None
            self._tail.next = None

        # Decrease the size of the list
        self._size -= 1

        # Return the data
        return data

    def __str__(self):
        """String method. Display the contents of the linked list."""
        return_string = ""
        # Set up a current node to walk the list.
        # Start it at the head node.
        current = self._head
        # Loop through the nodes until we hit None,
        # which will signify the end of the list.
        while current is not None:
            return_string += f"{current.data}{os.linesep}"
            # Move to the next node
            current = current.next
        return return_string

class Stack(LinkedList):
    """Stack data structure"""
    # Use add to front and remove from front
    def push(self, data):
        """Add a new element to the front of the linked list."""
        self.add_to_front(data)
    
    def pop(self):
        """Remove an element from the front."""
        if not self.is_empty:
            return self.remove_from_front()

class Queue(LinkedList):
    """Queue data structure"""
    # Use add to back and remove from front
    def enqueue(self, data):
        """Add a new element to the back of the linked list."""
        self.add_to_back(data)

    def dequeue(self):
        """Remove an element from the front."""
        if not self.is_empty:
            return self.remove_from_front()


# Notes:

# Droids sorted need to be in Astro, Jan, Util, Proto order.  No further ordering is needed.

# Droids total cost needs to be from least expensive to most expensive.

# For "isinstance", looks like i'll have to say "if droid model = isinstance(astroMech)" or something like that.

