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

       def filter(self, f):
        cur = self.head.next
        for i in range(0, cur.numElements):
            cur.elements[i] = f(cur.elements[i])
        return self.to_list()

    def map(self, f):
        cur = self.head.next
        while cur is not None:
            for i in range(0, cur.numElements):
                cur.elements[i] = f(cur.elements[i])
            cur = cur.next

    def reduce(self, f, initial_state):
        state = initial_state
        cur = self.head.next
        while cur is not None:
            for i in range(0, cur.numElements):
                state = f(state, cur.elements[i])
            cur = cur.next
        return state
