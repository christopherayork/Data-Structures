import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
# from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.cache = Queue()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        result = self.storage[key] if key in self.storage else None
        if not result: return
        else:
            self.cache.storage.move_to_end(result)
            return result.value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        result = self.storage[key] if key in self.storage else None
        if result:
            self.cache.storage.move_to_end(result)
            result.value = value
            return
        elif self.current >= self.limit:
            r = self.cache.dequeue()
            for k, v in self.storage.items():
                if r == v.value: self.storage[k] = None
            print(r)
            self.current -= 1
        self.cache.enqueue(value)
        self.storage[key] = self.cache.storage.tail
        self.current += 1
