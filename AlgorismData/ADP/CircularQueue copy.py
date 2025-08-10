class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[None]*self.capacity
        self.front=0
        self.rear=0
    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.front==(self.rear+1)%self.capacity
    def enqueue(self, item):
        if not self.isFull():
            self.rear=(self.rear+1)%self.capacity
            self.array[self.rear]=item
        else:
            pass
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.capacity
            return self.array[self.front]
        else:
            pass
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
        else:
            pass
    def size(self):
        return (self.rear-self.front+self.capacity)%self.capacity
    
    class CircularDeque(CircularQueue):
        def __init__(self,capacity=10):
            super().__init__(capacity)
        def addRear(self, e):
            return self.enqueue(e)
        def deleteFront(self):
            return self.dequeue()
        def getFront(self):
            return self.peek()
        
        def addFront(self, e):
            if not self.isFull():
                self.front=(self.front-1+self.capacity)%self.capacity
                self.array[self.front]=e
            else:
                pass
        
        def deleteRear(self):
            if not self.isEmpty():
                e=self.array[self.rear]
                self.rear=(self.rear-1+self.capacity)%self.capacity
                return e
            else:
                pass
        
        def getRear(self):
            if not self.isEmpty():
                return self.array[self.rear]
            else:
                pass

def hanoi(n,fr,tmp,to):
    if (n==1):
        print(f"원판1: {fr}->{to}")
    else:
        hanoi(n-1,fr,to,tmp)
        print(f"원판{n}: {fr}->{to}")
        hanoi(n-1,tmp,fr,to)
