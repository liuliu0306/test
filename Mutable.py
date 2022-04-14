class Node:
    def __init__(self, capacity=4):
        self.next = None
        self.numElements = 0  # 节点的元素个数
        self.elements = [None] * capacity
        self.cap = capacity  # 节点的容量


class UnrolledLinkedList:
    def __init__(self):
        self.total_size = 0  # 链表的总元素个数
        self.head, self.tail = Node(-1), Node(-1)  # 哨兵节点
        node = Node()
        self.head.next = node
        node.next = self.tail

    def size(self):
        return self.total_size

   
