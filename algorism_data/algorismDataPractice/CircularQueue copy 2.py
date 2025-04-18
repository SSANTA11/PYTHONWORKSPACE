class CircularQueue:
    def __init__(self,capacity=10):
        self.capacity=capacity
        self.array=[None]*self.capacity
        self.rear=0
        self.front=0
    def isEmpty(self):
        return self.rear==self.front
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
            self.array[self.front]=None
        else:
            pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
        else:
            pass
    def size(self):
        return (self.front-self.rear+self.capacity)%self.capacity