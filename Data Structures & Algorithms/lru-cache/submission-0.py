class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {} #key : val

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        
        # Move key to the end to mark it as recently used
        val = self.lru.pop(key)
        self.lru[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            # Remove old key to update both value and recency position
            self.lru.pop(key)
        elif len(self.lru) >= self.capacity:
            # Remove the first inserted key (least recently used)
            first_key = next(iter(self.lru))
            del self.lru[first_key]
        
        self.lru[key] = value
