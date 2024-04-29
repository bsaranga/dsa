import unittest

class MyTests(unittest.TestCase):

    def test_trivially_true(self):
        self.assertEqual(1, 1)