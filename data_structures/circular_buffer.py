class CircularBuffer():
    def __init__(self, size, pointer=0):
        self.size = size
        self.buffer = [None] * size
        self.pointer = pointer

    def append(self, value):
        self.buffer[self.pointer] = value
        self.pointer = (self.pointer + 1) % self.size