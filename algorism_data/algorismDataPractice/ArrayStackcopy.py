class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[None]*capacity
        self.top=-1
    def isEmpty(self):
        return self.top==1
    def isFull(self):
        return self.top==self.capacity-1
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass
    def push(self,e):
        if not self.isFull():
            self.top+=1
            self.array[self.top]=e
        else:
            pass
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array[self.top+1]
    def __str__(self):
        return (self.array[0:self.top+1])


a=ArrayStack()
a.push(int(input()))
a.push(int(input()))
a.push(int(input()))
print(a)