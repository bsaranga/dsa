class CircularBuffer():
    def __init__(self, size, start=0):
        self.start = start
        self.size = size
        self.buffer = [None] * size
        self.pointer = start

    def __str__(self) -> str:
        return f"Buffer: {self.buffer}"

    def append(self, value):
        self.buffer[self.pointer] = value
        self.pointer = (self.pointer + 1) % self.size

    def remove(self):
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.size