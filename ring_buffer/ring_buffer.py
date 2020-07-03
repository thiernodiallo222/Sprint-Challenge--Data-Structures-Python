class RingBuffer:
    def __init__(self, max):
        self.capacity = max
        self.pos=0
        self.storage =[]

    def append(self, item):
        if len(self.storage) != self.capacity:
            self.storage.append(item)
            if self.pos + 1 < self.capacity:
                self.pos += 1
            else:
                self.pos = 0
        else:
            self.storage[self.pos] = item
            if self.pos + 1 < self.capacity:
                self.pos += 1
            else:
                self.pos = 0
  
    def get(self):
        storage_without_none=[n for n in self.storage if n is not None]
        return storage_without_none
       
        