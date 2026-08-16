class LRUCache:

    def __init__(self, capacity: int):
        self.hmap={}
        self.capacity=capacity
        self.deck=deque()

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.deck.remove(key)
            self.deck.appendleft(key)
            return self.hmap[key]  
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.deck.remove(key)
            self.deck.appendleft(key)
            self.hmap[key]=value
        else:
            if len(self.deck)==self.capacity:
                remove=self.deck.pop()
                self.hmap.pop(remove)
            self.hmap[key]=value
            self.deck.appendleft(key)
            

