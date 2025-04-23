class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[None]*capacity
        self.front=0
        self.rear=0
    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.front==(self.rear+1)%self.capacity
    def enqueue(self, e):
        if not self.isFull():
            self.rear=(self.rear+1)%self.capacity
            self.array[self.rear]=e
        else:
            pass
    def dequeue(self):
        if not self.isEmpty():
            e=self.array[self.front]
            self.front=(self.front+1)%self.capacity
            return e
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.front]
        else:
            pass

map=[
    ['1','1','1','1','1','1'],
    ['e','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','0','1','1','1','1'],
    ['1','1','1','1','1','1']
    ]


def 