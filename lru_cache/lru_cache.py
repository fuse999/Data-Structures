from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit # Adding a limit to the cache
        self.held = 0 # starting held count too 0
        self.linked_list = DoublyLinkedList() # setting Cashed storage
        self.hashing_table = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # If there is the input key in the hashing_table
        if key in self.hashing_table:
            # Then move the DoublyLinkedList.tail to the front
            self.linked_list.move_to_front(self.linked_list.tail)
            # and return the Key
            return self.hashing_table[key]
        # if not ignore
        else:
            return None

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
        # If the key allredy in hashing_table then
        if key in self.hashing_table:
            # set the key value to input value
            self.hashing_table[key] = value
            return # stop est here
        # if there are more items held than the limit
        if self.held >= self.limit:
            # then del oldest cached value
            del self.hashing_table[self.linked_list.tail.value]
            self.linked_list.remove_from_tail()
        # Now lets add the key to the linked list
        self.linked_list.add_to_head(key)
        # set the key value to input value
        self.hashing_table[key] = value
        self.held += 1 # add +1 to held for tracking the limit
        
