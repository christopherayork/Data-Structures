"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if not self.head and not self.tail:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.head.prev = ListNode(value, None, self.head)
            self.head = self.head.prev
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if len(self) < 1: return None
        elif len(self) == 1:
            tmp = self.head
            self.head = None
            self.tail = None
        else:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return tmp.value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if not self.head and not self.tail:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            self.tail.next = ListNode(value, self.tail)
            self.tail = self.tail.next
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if len(self) == 1:
            tmp = self.tail
            self.tail = None
            self.head = None
        else:
            tmp = self.tail
            self.tail = self.tail.prev
            self.tail.prev.next = None
        self.length -= 1
        return tmp.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if len(self) <= 1: return
        self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if len(self) <= 1 or self.tail == node: return
        if self.head == node:
            self.head = node.next
            self.head.prev = None
        if node.prev: node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
        else:
            if self.head == node:
                self.head.next.prev = None
                self.head = self.head.next
            if self.tail == node:
                self.tail.prev.next = None
                self.tail = self.tail.prev
        self.length -= 1


    """Returns the highest value currently in the list"""
    def get_max(self):
        max = self.head.value
        next = self.head.next
        while next:
            if max < next.value: max = next.value
            next = next.next
        return max
