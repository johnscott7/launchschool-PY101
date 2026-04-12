class CircularBuffer:
    def __init__(self, spots):
        self._spots = spots
        self._slots = []
        self.counter = 0
        self.oldest_index = 0
        for _ in range(self._spots):
            self._slots.append(None)

    def put(self, value):
        if self._slots[self.counter] is not None:
            self.oldest_index = (self.oldest_index + 1) % self._spots

        self._slots[self.counter] = value
        self.counter += 1
        if self.counter == self._spots:
            self.counter = 0

    def get(self):
        oldest_item = self._slots[self.oldest_index]
        if oldest_item != None:
            self._slots[self.oldest_index] = None
            self.oldest_index += 1
            if self.oldest_index == self._spots:
                self.oldest_index = 0
        return oldest_item

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True
