class LRUCache:

    def __init__(self, capacity: int):
        self.length=capacity
        self.cache={}
        self.deque=deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.deque.remove(key)
        self.deque.appendleft(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key]=value
            self.deque.remove(key)
            self.deque.appendleft(key)
        else:
            if (len(self.cache)==self.length):
                ele=self.deque.pop()
                del self.cache[ele]
            self.cache[key]=value
            self.deque.appendleft(key)

