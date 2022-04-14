import unittest
from hypothesis import given, settings
from Mutable import UnrolledLinkedList,Node
import hypothesis.strategies as st


class TestMutableUnrolled_linked_list(unittest.TestCase):


    def test_size(self):
        lst = UnrolledLinkedList()
        self.assertEqual(lst.size(), 0)
        lst.set(0, 'a')
        self.assertEqual(lst.size(), 1)
        lst.set(1, 'b')
        self.assertEqual(lst.size(), 2)

        
if __name__ == '__main__':
    unittest.main()
