class DNode:
    def __init__ (self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next
class LinkedList:
    def __init__( self ):
        self.head = None
    def isEmpty( self ):
        return self.head == None
    def isFull( self ):
        return False

    def getNode(self, pos) :
        if pos < 0 :
            return None
        node = self.head
        while pos > 0 and node != None :
            node = node.next
            pos -= 1
        return node
    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None :
            return None
        else :
            return node.data
    def insert(self, pos, elem) : # 생각보다 시간을 왜 썼다. 해당 부분에 의해 보고서가 촉박해지지 않을까?
        before = self.getNode(pos-1)
        after = self.getNode(pos) # 놓진 부분;; 주의하자
        if before == None :
            node=DNode(elem, None, after)
            self.head = node
            if after is not None: #  인덱스 0과 아무것도(after) 없을 때...!
                after.prev = node
        else :
            node=DNode(elem, before, None)
            before.next=node
            if after is not None: # 이번에도 after가 없을 때
                after.prev=node

    def delete(self, pos) :# 사제 되는 요소를 가르키는 것 또한 없애야된다
        before = self.getNode(pos-1)
        if before == None :
            if self.head is not None :
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev=None
        elif before.next != None :
            before.next = before.next.next
            if before.next is not None:
                before.next.prev=before

    def size( self ) :
        node = self.head
        count = 0
        while node is not None :
            node = node.next
            count += 1
        return count

    def printForward(self):
        if not self.isEmpty():
            node=self.getNode(0)
            while node is not None:
                print(node.data, end=" ")
                node=node.next

    def printReverse2(self):
        if not self.isEmpty():
            node=self.getNode(self.size()-1)
            while node is not None:
                print(node.data)
                node=node.prev

    def append2(self, e):
        if self.isEmpty() is not True:
            node=self.getNode(self.size()-1)
            newNode=DNode(e)
            node.next=newNode
            newNode.prev=node
        else:
            self.head=DNode(e)

    def merge(self,B):
        BSize=B.size()
        for i in range(BSize):
            self.append2(B.getEntry(0))
            B.delete(0)

