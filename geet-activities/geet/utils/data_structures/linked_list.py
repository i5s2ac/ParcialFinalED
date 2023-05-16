'''
[Data Structure] Linked List implementation.
'''


class Node:
    '''
    Node object.

    Attributes:
        hash (str): commit's hash
        message (str): commit's message
        author (str): user's name
        email (str): user's email
        next (Node): pointer to next node in list

    ⬇ Your code starts here:
    '''
    def __init__(self, hash: str, message: str, author: str, email: str):
        self.hash = hash
        self.message = message
        self.author = author
        self.email = email
        self.next = None
    '''
    ⬆ Your code ends here.
    '''

class LinkedList:
    '''
    Linked List object.

    Attributes:
        start (Node): pointer to first node in list

    Methods:
        __init__(self)
        __iter__(self)
        traverse(self)
        insert_first(self, node)
        insert_last(self, node)
        remove(key)
        reverse(self)

    ⬇ Your code starts here:
    '''
    def __init__(self):
        self.start = None

    def __iter__(self):
        current = self.start
        while current is not None:
            yield current
            current = current.next

    def traverse(self):
        for node in self:
            print(node.hash, node.message, node.author, node.email)

    def insert_first(self, node):
        node.next = self.start
        self.start = node

    def insert_last(self, node):
        if self.start is None:
            self.start = node
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = node

    def remove(self, key):
        if self.start is None:
            return

        if self.start.hash == key:
            self.start = self.start.next
            return

        current = self.start
        while current.next is not None:
            if current.next.hash == key:
                current.next = current.next.next
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.start

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.start = prev
    '''
    ⬆ Your code ends here.
    '''
