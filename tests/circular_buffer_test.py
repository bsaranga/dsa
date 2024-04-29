from unittest import TestCase
from data_structures.circular_buffer import CircularBuffer


class CircularBufferTests(TestCase):

    def test_circular_buffer_size(self):
        cb = CircularBuffer(5)
        self.assertEqual(cb.size, 5)
    
    def test_circular_buffer_append(self):
        cb = CircularBuffer(5)
        cb.append(1)
        cb.append(2)
        cb.append(3)
        self.assertEqual(cb.buffer, [1, 2, 3, None, None])
    
    def test_circular_buffer_wrap(self):
        cb = CircularBuffer(3)
        cb.append(1)
        cb.append(2)
        cb.append(3)
        cb.append(4)
        self.assertEqual(cb.buffer, [4, 2, 3])

    def test_circular_buffer_pointer(self):
        cb = CircularBuffer(3)
        cb.append(1)
        cb.append(2)
        cb.append(3)
        self.assertEqual(cb.pointer, 0)
    
    def test_circular_buffer_pointer_wrap(self):
        # [None, 1, 2]
        cb = CircularBuffer(3, 1)
        cb.append(1)
        cb.append(2)
        cb.append(3)
        self.assertEqual(cb.pointer, 1)