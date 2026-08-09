class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.deck=deque()
        self.hmap={}

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.deck.remove(key)
            self.deck.append(key)
            return self.hmap[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        
        if key in self.hmap:
                self.deck.remove(key)

        else:
            if self.capacity==len(self.hmap):
                old=self.deck.popleft()
                del self.hmap[old]
        
        self.deck.append(key)
        self.hmap[key]=value

        return 