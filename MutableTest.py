import unittest
from hypothesis import given
from Mutable import *
import hypothesis.strategies as st


class TestMutableUnrolled_linked_list(unittest.TestCase):


    def test_size(self):
        lst = UnrolledLinkedList()
        self.assertEqual(lst.size(), 0)
        lst.set(0, 'a')
        self.assertEqual(lst.size(), 1)
        lst.set(1, 'b')
        self.assertEqual(lst.size(), 2)


    def test_from_list(self):
        lst = UnrolledLinkedList()
        lst.from_list([])
        self.assertEqual(lst.to_list(), [])
        lst = UnrolledLinkedList()
        lst.from_list(['a'])
        self.assertEqual(lst.to_list(), ['a'])
        lst = UnrolledLinkedList()
        lst.from_list(['a', 'b'])
        self.assertEqual(lst.to_list(), ['a', 'b'])


    def test_to_list(self):
        lst = UnrolledLinkedList()
        self.assertEqual(UnrolledLinkedList().to_list(), [])
        lst.set(0, 'a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.set(1, 'b')
        self.assertEqual(lst.to_list(), ['a', 'b'])

    def test_set(self):
        lst = UnrolledLinkedList()
        lst.set(0, 'a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.set(1, 'b')
        self.assertEqual(lst.to_list(), ['a', 'b'])


    def test_get(self):
        lst = UnrolledLinkedList()
        lst.set(0, 'a')
        lst.set(1, 'b')
        self.assertEqual(lst.get(0), 'a')
        self.assertEqual(lst.get(1), 'b')

    def test_remove(self):
        lst = UnrolledLinkedList()
        lst.set(0, 'a')
        lst.set(1, 'b')
        lst.set(2, 'c')
        lst.remove(2)
        self.assertEqual(lst.to_list(), ['a', 'b'])
        lst.remove(1)
        self.assertEqual(lst.to_list(), ['a'])
        lst.remove(0)
        self.assertEqual(lst.to_list(), [])

    def test_is_member(self):
        x = ['a', 'b', 'c']
        lst = UnrolledLinkedList()
        lst.from_list(x)
        index = lst.is_member('b')
        self.assertEqual(index, 1)

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

    def test_iter(self):
        x = [1, 2, 3]
        lst = UnrolledLinkedList()
        lst.from_list(x)
        tmp = []
        for e in lst.head.next.elements:
            if e != None:
                tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(lst.to_list(), tmp)

        i = iter(UnrolledLinkedList())
        self.assertRaises(StopIteration, lambda: next(i))


        
if __name__ == '__main__':
    unittest.main()
