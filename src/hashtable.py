# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return self._hash_djb2(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_value = 5381

        for char in key:
            hash_value = (hash_value << 5) + hash_value + ord(char)
        
        return hash_value



    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
    
        # Create new node
        new_node = LinkedPair(key,value)
        # Get current position
        position = self._hash_mod(key)
        # Get the current node at the position
        current_node = self.storage[position]
        if current_node is None:
            self.storage[position] = new_node
            return

        elif current_node:
            # Traverse the list
            while current_node:
                # Check if the key already exists and update
                if (self._hash(key) == self._hash(current_node.key)):
                    if ( value == current_node.value):
                        return
                    else:
                        current_node.value = value
                        return 
                elif current_node.next is None:
                    current_node.next = new_node
                    return
                current_node = current_node.next
           


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash(key)
        # Get item position
        position = self._hash_mod(key)
        # Get item
        item = self.storage[position]
        while item is not None:
            if self._hash(item.key) == hashed_key:
                self.storage[position] = item.next
                return key
            item = item.next
     
        print('Item not found!!!')
        return 


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash(key)
        for hash in self.storage:
            if hash is not None and self._hash(hash.key) == hashed_key:
                return hash.value
            if hash is not None and hash.next:
                next = hash.next
                while next:
                    if self._hash(next.key) == hashed_key:
                        return next.value
                    next = next.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Create new storage
        new_storage = [None]* self.capacity * 2
        # Iterate over the old storage
        # Copy items to the new storage
        for i, item in enumerate(self.storage):
            # Check if the item is not None
            if item is not None:

                # Get a position for the item
                postion = self._hash_mod(item.key)
                # Get the item already in the position
                current_item = new_storage[postion]

                # Check if there's no collision
                if current_item is None:
                    # Insert the item in position
                    new_storage[postion] = item
                # There's a collision, now traverse the list and insert the item at the right position
                else:
                    while current_item:

                        # Check if it is the right position to insert the item
                        if current_item.next is None:
                            current_item.next = item
                        else:
                            current_item = current_item.next
        # destroy the old storage memory
        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print(ht._hash('ss'))
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
