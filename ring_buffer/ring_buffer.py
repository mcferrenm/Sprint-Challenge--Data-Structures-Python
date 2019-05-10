class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity
        self.index = 0

    def append(self, item):
        print(self.index)

        self.storage[self.index] = item

        if self.index > 3:
            self.index = 0
        else:
            self.index += 1

    def get(self):
        return [i for i in self.storage if i]


buffer = RingBuffer(5)

print(buffer.get())

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')

print(buffer.get())
