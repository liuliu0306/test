# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:28:24 2022

@author: liurh
"""
import unittest
from hypothesis import given, settings
import hypothesis.strategies as st
from UnrolledLinkedList import UnrolledLinkedList, Node



class TestMutableULList(unittest.TestCase):
    
    # first we use unit test!
    def test_add_and_remove(self):
        print('\nTesting add and remove...')
        ull = UnrolledLinkedList(4)
        self.assertEqual(ull.add(1),None)
        # lst.insert(0, 'a')
        self.assertEqual(ull.add(2),None)
        self.assertEqual(ull.remove(1),None)
        self.assertEqual(ull.remove(2),None)
        
    def test_traversal(self):
        print('Testing traversal...')
        ull = UnrolledLinkedList(4)
        self.assertEqual(ull.traversal(),None)

    def test_to_list(self):
        print('Testing to_list...')
        ull = UnrolledLinkedList(4)
        ull.add(1)
        ull.add(2)
        ull.add(3)
        self.assertEqual( type(ull.to_list()), list)

    def test_from_list(self):
        print('Testing from_list...')
        dlist = [1,2,3,4]
        ull = UnrolledLinkedList(4)
        self.assertEqual( ull.from_list( dlist ), None )

    def test_size(self):
        print('Testing size...')
        ull = UnrolledLinkedList(4)
        ull.add(1)
        ull.add(2)
        ull.add(3)
        ull.add(4)
        self.assertEqual( ull.size(),4 )


    def test_set_element(self):
        print('Testing set_element...')
        ull = UnrolledLinkedList(4)
        key, value = 1,999
        ull.from_list([1,2,3,4])
        self.assertEqual( ull.set_element(key, value).to_list(),[1,999,3,4] )
    
    
    def test_ull_filter(self):
        print('Testing ull_filter...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1,2,3,4])
        ull.ull_filter()
        self.assertEqual( ull.to_list(),[2,4] )
        
       
    def test_ull_map(self):
        print('Testing ull_map...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1,2,3,4])
        ull.ull_map(lambda x:x**2)
        self.assertEqual( ull.to_list(),[1,4,9,16] )
        
        
    def test_ull_reduce(self):
        print('Testing ull_reduce...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1,2,3,4])   
        self.assertEqual( ull.ull_reduce(lambda x,y:x+y),10 )
        
    def test_empty_and_concat(self):
        print('Testing empty_and_concat...')
        ull = UnrolledLinkedList(4)
        self.assertEqual( ull.empty(),1 )
        self.assertEqual( ull.concat(2,3),6 )
        
        
    def test_iterate(self):
        print('Testing iterate...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1,2,3,4])
        arr = ull.to_list()
        for cyi in range(4):
            self.assertEqual( ull.__next__(),arr[cyi] )
    
    def test_reverse(self):
        print('Testing reverse...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1,2,3,4])
        b = ull.reverse()
        self.assertEqual( b.to_list(),[4,3,2,1])
    
    def test_is_member(self):
        print('Testing is_member...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1,2,3,4])
        b = ull.is_member(3)
        self.assertEqual( b,True)
        b = ull.is_member(5)
        self.assertEqual( b,False)
        
    # ---------------------------------------------
    # then we use PBT test!

    @settings(max_examples=10)
    @given(st.lists(st.integers()))
    def test_reverse_PBT(self, a):
        ull = UnrolledLinkedList(4)
        ull.from_list(a)
        b = ull.reverse()
        if( b!= None ):
            temp = ull.reverse().to_list()
            if( (a.reverse() != None) & (temp != []) & (type(temp.reverse()) != 'NoneType') & (type(a.reverse()) != 'NoneType') ):
                self.assertEqual(temp,a.reverse())
        
    @settings(max_examples=10)
    @given(st.integers())
    def test_is_member_PBT(self, a):
        ull = UnrolledLinkedList(4)
        ull.from_list([1,2,3,a])
        b = ull.is_member(a)
        self.assertEqual(b, True)

        
if __name__ == '__main__':
    unittest.main()



















