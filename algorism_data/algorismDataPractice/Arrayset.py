class ArraySet:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[None]*capacity
        self.size=0
    def isEmpty(self):
        return self.size==0
    def isFull(self):
        return self.size==self.capacity
    def __str__(self):
        return str(self.array[0:self.size])
    def contains(self, e):
        for i in range(self.size):
            if self.array[i]==e:
                return True
        return False
    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size]=e
            self.size+=1
    def delete(self,e):
        for i in range(self.size):
            if self.array[i]==e:
                self.array[i]=self.array[self.size]
                return
    def union(self, setB):
        setC=ArraySet()
        for i in range(self.size):
            setC.insert(setB.array[i])
        for i in range(setB.size):
            if not setC.contains(self.array[i]):
                setC.insert(setB.array[i])
        return setC