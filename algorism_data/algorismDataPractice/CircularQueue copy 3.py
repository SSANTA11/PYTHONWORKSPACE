class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[None]*capacity
        self.front=0
        self.rear=0
    def isEmpty(self):
        return self.top==-1
    def isFull(self):
        return self.rear==self.front