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
        
    def test_filter(self):
        def f(x):
            res = x + 2
            return res

        x = [3, 4, 5]
        lst = UnrolledLinkedList()
        lst.from_list(x)
        lst.filter(f)
        self.assertEqual([5, 6, 7], lst.to_list())


    def test_map(self):
        lst = UnrolledLinkedList()
        lst.map(str)
        self.assertEqual(lst.to_list(), [])

        lst = UnrolledLinkedList()
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ["1", "2", "3"])

        lst = UnrolledLinkedList()
        lst.from_list([1, 2, 3])
        lst.map(lambda x: x + 1)
        self.assertEqual(lst.to_list(), [2, 3, 4])


    def test_reduce(self):
        # sum of empty list
        lst = UnrolledLinkedList()
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)

        # sum of list
        lst = UnrolledLinkedList()
        lst.from_list([1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)
        # size
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = UnrolledLinkedList()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda st, _: st + 1, 0), lst.size())

        
if __name__ == '__main__':
    unittest.main()
