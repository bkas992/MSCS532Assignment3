class HashTable:

    # Initialize table with empty lists for each index
    def __init__(self, size=100):
        self.table = [[] for _ in range(size)]

    
    # Simple hash function to compute the index
    def hash_func(self, key):
        return hash(key) % len(self.table)

    # Insert key-value pair, update if key already exists
    def insert(self, key, value):
        index = self.hash_func(key)
        for pair in self.table[index]:
            if pair[0] == key:  # Key found, update value
                pair = (key, value)  # Replace existing pair
                return
        self.table[index].append((key, value))  # Key not found, add new pair

    # Search for key and return associated value
    def search(self, key):
        index = self.hash_func(key)
        for pair in self.table[index]:
            if pair[0] == key:  # Key found
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        # Delete key-value pair by key
        index = self.hash_func(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:  # Key found
                del self.table[index][i]  # Remove the pair
                return