class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[None]*capacity
        self.front=0
        self.rear=0
    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.rear==self.front
    def enqueue(self,item):
        if not self.isFull():
            self.rear=(self.rear+1)%self.capacity
            self.array[self.rear]=item
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.capacity
        return self.array[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
    def size(self):
        return (self.rear-self.front+self.capacity)%self.capacity
    def __str__(self):
        if self.rear>self.front:
            return str(self.array[self.front+1:self.rear+1])
        return str(self.array[self.front+1:self.capacity]+self.array[0:self.rear+1])