
class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]
        self.A = (5**0.5 - 1) / 2  # The golden ratio

    def _hash(self, key):
        return int(self.capacity * ((self.A * key) % 1))

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:  # If the key already exists, update the value
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.size += 1

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                self.size -= 1
                return
        print("Key not found.")

    def load_factor(self):
        return self.size / self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]
        for chain in self.table:
            for key, value in chain:
                new_index = int(new_capacity * ((self.A * key) % 1))
                new_table[new_index].append([key, value])
        self.capacity = new_capacity
        self.table = new_table