# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:40:54 2022

@author: liurh
"""
class Node:
    def __init__(self):
      self.length = 0
      self.array = []
      self.next = None


class UnrolledLinkedList:
    def __init__(self, capacity):
      # maximum capacity of an array in node
      self.capacity = capacity
      self.head = None
      self.tail = None
      self.ull_iter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.ull_iter +=1
        return self.to_list()[self.ull_iter]

    # this method inserts the given value in the list
    def add(self, value):
        if self.head == None: #unrolled linked is empty
            self.head = Node()
            self.head.array.append(value) # add the value
            self.head.length += 1
            self.tail = self.head
        elif self.tail.length + 1 <= self.capacity: # current node's capacity is not full
            self.tail.array.append(value) # add the given value
            self.tail.length += 1
        else: # current node's capacity is full
            new_node = Node() # create a new node
            # move final half of elements from the current node to the new node
            half_length = self.tail.length//2 
            new_node.array.extend(self.tail.array[half_length:])
            new_node.array.append(value) # add the given value to the new node
            # Update
            new_node.length = len(new_node.array) # set the length of the new node's array
            self.tail.length = half_length # update the length of the current node's array
            self.tail.next = new_node # make current node next pointer refer to the new node
            self.tail = new_node # update the tail

    # prints all the elements of the unrolled linked list
    def traversal(self):
        temp = self.head
        while temp:
            for i in range(0, temp.length):
                print(temp.array[i], end="\t")
            print()
            temp = temp.next

    # This method removes the first appearance of the given value
    def remove(self, value, ull_type='value'):
      # find the given value and delete it 
      temp = self.head
      count = -1
      while temp:
        for i in range(0, temp.length):
          count += 1
          if (type(temp.array[i]) == dict) & (ull_type == 'dict'):
              temp.array[i] = list(temp.array[i].keys())[0]
          elif (ull_type == 'list'):
              if(count == value):     
                  temp.array[i] = value
              else:
                  continue
          if temp.array[i] == value:
            temp.array.pop(i) # remove the given value from the array
            temp.array.append(None)
            temp.length -= 1 # decrease the length
            # if the current node's length is less than 50% then move elements from next node's array to the current one
            while temp.length < (self.capacity//2) and temp.next:
              temp.array[temp.length] = temp.next.array.pop(0)
              temp.length +=1
              temp.next.length -= 1
            # if the next node's length is less than 50%  then merge the two halves
            if temp.next and temp.next.length < (self.capacity//2) : 
              temp.array[temp.length:temp.length+temp.next.length] = temp.next.array[:temp.next.length]
              temp.length += temp.next.length
              # deleted_node = temp.next
              temp.next = temp.next.next
              # del deleted_node
            return
        temp = temp.next
      raise ValueError(f'Value {value} does not exist in the list')

    def to_list(self):
        # organize the data with an array
        p = self.head
        arr = []
        while p:
            arr.extend(p.array[0:p.length])
            p = p.next
        return arr

    def from_list(self, arr=[]):
        # add a list to UnrolledLinkedList
        for cyi in range(len(arr)):
            self.add(arr[cyi])

    def size(self):
        return len(self.to_list())

    def reverse(self):
        ull_list = self.to_list()
        ull_list.reverse()
        self = UnrolledLinkedList(self.capacity)
        self.from_list(ull_list)
        return self

    def is_member(self, value):
        p = self.head
        while p:
            if(value in p.array):
                # if value is in p.array, find successfully
                return True
            p = p.next
        # if not in the UnrolledLinkedList...
        return False

    def set_element(self, idx, value):
        # update an element according index and value
        ull_list = self.to_list()
        ull_list[idx] = value
        self = UnrolledLinkedList(self.capacity)
        self.from_list(ull_list)
        return self

    def ull_filter(self, condition='iseven'):
        if (condition == 'iseven'):
            [self.remove(cyi,'list') for cyi in range(self.size()//2)]

    def ull_map(self,function):
        p = self.head
        while p:
            for cyi in range(p.length):
                p.array[cyi] = function(p.array[cyi])
            p = p.next

    def ull_reduce(self,function):
        # iterative processing
        ull_list = self.to_list()
        for _ in range( len(ull_list)-1 ):
            ull_list[0] = function(ull_list[0], ull_list[1])
            ull_list.pop(1)
        return ull_list[0]

    def empty(self):
        return 1

    def concat(self, a, b):
        return a*b

