class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage=[]

    def append(self, item):
        if len(self.storage == self.capacity):
            self.storage.pop(0)
            self.storage.append(item)
        self.storage.append(item)
        self.capacity += 1
        else:
            self.capcity += 1
            self.storage.append(item)
            

    def get(self):
        if len(self.storage) > 0:
            return self.storage
        return None
        