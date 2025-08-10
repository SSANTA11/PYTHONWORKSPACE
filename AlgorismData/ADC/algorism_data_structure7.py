
# 스택을 응용한 연결된 리스트
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def isFull(self):
        return False

    def push(self, e):
        self.top = Node(e, self.top)

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data

    def size(self):
        node = self.top
        count = 0
        while node is not None:
            node = node.link
            count += 1
        return count

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def __str__(self):
        arr = []
        node = self.top
        while node is not None:
            arr.append(node.data)
            node = node.link
        return str(arr)

class Linkedlist:
    def __init__(self):
        return self.head==None
    def isFul(Self):
        return False
    def getNode(self, pos):
        if pos<0:
            return None
        node=self.head
        while pos > 0 and node != None:
            node = node.link
            pos-=1
        return node
    def getEntry(self)