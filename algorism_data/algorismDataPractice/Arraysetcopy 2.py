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
    def contains(self,e):
        for i in range(self.size):
            if e==self.array[i]:
                return True
            else:
                return False
    def insert(self,e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size]=e
            self.size+=1
        else:
            pass
    def delete(self,e):
        for i in range(self.size):
            if self.array[i]==e:
                self.array[i]=self.array[self.size]
            self.size-=1

    def union(self, setB):
        setC=ArraySet()
        for i in range(setB.size):
            setC.insert(setB.array[i])
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

    def intersect(self, setB):
        setC=ArraySet()
        for i in range(setB.size):
            if self.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC
    def difference(self,setB):
        setC=ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC